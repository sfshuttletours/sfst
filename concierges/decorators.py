from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def only_concierges(function):
    def view_func(request, *args, **kwargs):
        user = request.user
        try:
            contact = user.contact_set.all()[0]
        except IndexError:
            return HttpResponseRedirect(reverse('home'))
        try:
            concierge = contact.concierges.all()[0]
        except AttributeError:
            return HttpResponseRedirect(reverse('home'))
        return function(request, concierge, *args, **kwargs)
    return view_func
