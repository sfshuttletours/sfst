from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from satchmo_store.shop.models import Order
from adjustments.forms import AdjustmentDeleteForm, AdjustmentMoveForm, \
    AdjustmentRefundRequestForm, AdjustmentRefundForm, AdjustmentCreditVoucherForm, \
    AuthorizeNetError
from common.http import JsonResponse

FORMS = {
    'delete': AdjustmentDeleteForm,
    'move': AdjustmentMoveForm,
    'request_refund': AdjustmentRefundRequestForm,
    'refund': AdjustmentRefundForm,
    'make_credit_voucher': AdjustmentCreditVoucherForm
}

@login_required
@staff_member_required
def main(request, order_id, action_type):
    order = get_object_or_404(Order, id=int(order_id))
    success = True
    data = {}
    
    if action_type == 'refund' and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('order_detail', args=[order_id]))
    
    FormClass = FORMS[action_type]
    
    if request.method == 'POST':
        form = FormClass(request, order, request.POST)
        if form.is_valid():
            try:
                msg = form.do_it()
                messages.success(request, msg)
            except AuthorizeNetError, e:
                messages.error(request, 'There was an error with calling Authorize.NET: %s' % e)
            data['redirect'] = True
        else:
            success = False
    else:
        form = FormClass(request, order)
        
    if action_type == 'refund':
        action_type = 'Refund/Void/Reject'
    data['html'] = render_to_string('adjustments/form.html', {
                    'form': form, 
                    'action_type': action_type.replace('_', ' '),
                    'request': request
                    })
    return JsonResponse(data, success=success)    
