from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from _include.Chimera.models import Order


def orders(request):
    order_list = list(Order.objects.all().order_by('order_status').values())
    response = render(request, 'page/order/orders.html', Context({'order_list': order_list}))
    return HttpResponse(response)
