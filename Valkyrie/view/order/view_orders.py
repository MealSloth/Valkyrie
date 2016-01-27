from django.http import HttpResponse
from django.shortcuts import render


def orders(request):
    response = render(request, 'page/order/orders.html')
    return HttpResponse(response)
