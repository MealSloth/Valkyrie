from _include.Chimera.Chimera.models import Order
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def order_delete(request, order_id):
    order = Order.objects.filter(pk=order_id)
    if order.count() > 0:
        order = order[0]
    else:
        return HttpResponseRedirect('/orders')

    try:
        order.delete()
    except StandardError:
        return HttpResponseRedirect(reverse('order', args=[order.id, ]))

    return HttpResponseRedirect('/orders')
