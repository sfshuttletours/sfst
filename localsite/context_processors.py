from django.core.urlresolvers import reverse

from localsite.models import TourType, SiteSkin
from adjustments.models import Adjustment

from satchmo_store.contact.models import Contact


def concierge(request):
    """
    Put the concierge on the context
    """
    try:
        contact = Contact.objects.from_request(request)
        return {'concierge': contact.concierge}
    except: return {}

def site_skin(request):
    """
    So that every template (including the base templates) have the current skin instance to modify the header link/image,
    custom css, TOC link/text etc.
    """
    d = {'site_skin': request.site_skin}
    if request.user.is_staff:
        d.update({
            'default_skin': SiteSkin.objects.get(is_default=True),\
            'non_default_skins': SiteSkin.objects.filter(is_default=False)
        })
    return d

def skins(request):
    """
    Adds list of skins to every request to use to generate the navbar tour booking links for the various sites.
    """
    d = {'skins': SiteSkin.objects.all()}
    return d


def affilate(request):
    ctx = {
        'affiliate': request.session.get('affiliate', None),
        'Adjustment': Adjustment,
    }
    return ctx

def satchmo_cart_tours(request):
    """
    To be used in the cart template only to show all the tours user can add etc.
    """
    d = {}
    if request.path == reverse('satchmo_cart'):
        d['tour_types_for_cart'] = TourType.objects.filter(active=True, categories__site_skins=request.site_skin).exclude(rollover_off='')

    return d
