from math import fabs
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from resellers.models import Reseller
from concierges.models import Concierge
from localsite.models import SiteSkin, OverbookingAttempt
from localsite.session import SessionManager


SITE_SKIN_PARAM = 'skin'

class SiteSkinMiddleware(object):
    def process_request(self, request):
        site_skin_code = request.GET.get(SITE_SKIN_PARAM)

        if site_skin_code:
            qset = SiteSkin.objects.filter(code=site_skin_code)
            if qset:
                site_skin_id = qset.get().id
            else:
                site_skin_id = self.__get_default_site_skin().id

            # store it in the session
            SessionManager(request).site_skin(site_skin_id)
        elif SessionManager(request).site_skin():
            site_skin_id = SessionManager(request).site_skin()

            # store it in the session
            SessionManager(request).site_skin(site_skin_id)
        elif 'site_skin' in request.COOKIES:
            site_skin_id = request.COOKIES['site_skin']
        else:
            site_skin_id = self.__get_default_site_skin().id

        qset = SiteSkin.objects.filter(id=site_skin_id)
        if qset:
            request.site_skin = qset.get()
        else:
            request.site_skin = self.__get_default_site_skin()

    def process_response(self, request, response):
        site_skin_code = request.GET.get(SITE_SKIN_PARAM)
        has_site_skin = hasattr(request, 'site_skin') and SessionManager(request).site_skin()
        if site_skin_code or has_site_skin:
            response.set_cookie('site_skin', request.site_skin.id if has_site_skin else site_skin_code)
        return response

    def __get_default_site_skin(self):
        return SiteSkin.objects.get(is_default=True)

class AffiliateMiddleware(object):

    def process_request(self, request):
        code = request.GET.get('CODE', None)
        if code is None:
            code = request.GET.get('code', None)

        if code:
            affiliate = None
            try:
                affiliate = Reseller.objects.get(code=code)
            except Reseller.DoesNotExist:
                try:
                    affiliate = Concierge.objects.get(code=code)
                except Concierge.DoesNotExist:
                    pass

            if affiliate:
                request.session['affiliate'] = affiliate


# TODO Redirect to /affiliate-checkout/ if there is an affiliate and user hits /checkout/ and vice versus

class CheckoutMiddleware(object):
    """Verify if shopper should be forced to pay or allowed to book free tours.

    It needs to happen after the AffiliateMiddleware above.
    """

    def process_request(self, request):
        """Redirect user to proper checkout page if necessary.

        If user is logged in as affiliate or admin they are allowed to book free
        tours so they get to see /affilate-checkout/.

        If not, they must use the regular checkout page.
        """

        affilate_checkout_url = reverse('affiliate_checkout')
        regular_checkout_url = reverse('satchmo_checkout-step1')

        # Allows a priviledged user to opt to charge a card once
        # Value will be 1 or 0, for True or False
        request.session.setdefault('FORCE_CHARGE', 0)
        force_charge = request.GET.get('force_charge', None)
        if force_charge is not None:
            request.session['FORCE_CHARGE'] = int(force_charge)

        if request.path == affilate_checkout_url:
            if request.user.is_authenticated() and request.user.can_book_free_tours():
                pass
            else:
                return HttpResponseRedirect(regular_checkout_url)

        if request.path == regular_checkout_url:
            if request.session['FORCE_CHARGE']:
                pass
            elif request.user.is_authenticated() and request.user.can_book_free_tours():
                return HttpResponseRedirect(affilate_checkout_url)


'''
Middleware to detect if items in cart no longer have any inventory left.
Thus, it prevents the checking out of out-of-stock items, that may have been
switched to inactive or sold out after the customer added them to their cart.
Avoids negative inventory numbers.
'''

from django.utils.translation import ugettext as _
from django.contrib import messages

from payment.views.contact import contact_info_view
from payment.modules.authorizenet.views import pay_ship_info
from payment.modules.authorizenet.views import confirm_info
from localsite.views import affiliate_checkout, home
from satchmo_store.shop.models import Cart, CartItem, NullCart, NullCartItem
from satchmo_store.shop.signals import satchmo_cart_changed

checkviews = [home, contact_info_view, pay_ship_info, confirm_info, affiliate_checkout]

class SNIMiddleware(object):
    """
    Checks if cart has items that don't have enough inventory.
    """
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func in checkviews:
            cart = Cart.objects.from_request(request, create=False)
            outofstock = False
            product_vars = {}
            for cartitem in cart:
                product_vars[cartitem.product.productvariation.parent.product.name] = {'count': 0, 'delete': False, 'parent_product': cartitem.product.productvariation.parent.product}
            for cartitem in cart:
                stock = cartitem.product.productvariation.parent.product.items_in_stock - cartitem.product.productvariation.parent.product.total_sold
                product_vars[cartitem.product.productvariation.parent.product.name]['count'] += int(cartitem.quantity)
                if not cartitem.product.productvariation.parent.product.in_stock() \
                or not cartitem.product.productvariation.parent.product.active \
                or stock < product_vars[cartitem.product.productvariation.parent.product.name]['count']:
                    product_vars[cartitem.product.productvariation.parent.product.name]['delete'] = True
                    outofstock = True
            for k, v in product_vars.items():
                if v['delete']:
                    tour_product = cartitem.product.productvariation.parent.product.tourproduct
                    cart.cartitem_set.filter(product__productvariation__parent__product=v['parent_product']).delete()
                    if SessionManager(request).do_record_overbook_attempt(tour_product):
                        overbooked_amount = fabs(cartitem.product.productvariation.parent.product.items_in_stock - cartitem.product.productvariation.parent.product.total_sold - v['count'])
                        tour_product.overbooking_attempts += overbooked_amount
                        tour_product.save()
                        overbooking = OverbookingAttempt.objects.create(tour=tour_product, num_overbooked=overbooked_amount)
                        overbooking.save()

            if outofstock:
                messages.error(request, 'Out-of-stock items have been removed from your cart.  Please review your order before checking out again. Thank you.')
                satchmo_cart_changed.send(cart, cart=cart, request=request)
                return HttpResponseRedirect(reverse('satchmo_cart'))
        return None
