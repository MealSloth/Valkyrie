from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from _include.Chimera.Chimera.models import Order


def order(request, order_id):
    current_order = Order.objects.filter(id=order_id).values()[0]
    response = render(request, 'page/order/order.html', Context({"order": current_order}))
    return HttpResponse(response)
