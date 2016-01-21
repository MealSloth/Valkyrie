from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
import MySQLdb


def home(request):
    response = render(request, 'page/home.html')
    return HttpResponse(response)


def users(request):
    # mdb = MySQLdb.connect(host='chimera-1196:chimera-1196-cloudsqlg1-instance', user='root', db='chimera_prod01')
    # name = mdb.query("SELECT first_name FROM user WHERE id=1")
    # response = render(request, 'page/users.html', Context({"name": name}))
    response = render(request, 'page/users.html')
    return HttpResponse(response)


def posts(request):
    response = render(request, 'page/posts.html')
    return HttpResponse(response)


def orders(request):
    response = render(request, 'page/orders.html')
    return HttpResponse(response)
