from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from Valkyrie.models import User


def home(request):
    response = render(request, 'page/home.html')
    return HttpResponse(response)


def users(request):
    user_list = list(User.objects.all().values())
    response = render(request, 'page/users.html', Context({"user_list": user_list}))
    return HttpResponse(response)


def posts(request):
    response = render(request, 'page/posts.html')
    return HttpResponse(response)


def orders(request):
    response = render(request, 'page/orders.html')
    return HttpResponse(response)


# Not to be used right now
def generate_users():
    for i in range(0, 1):
        user = User(i, i, i, i, i, i, i,
                    "TestPerson" + str(i) + "@gmail.com",
                    "Test " + str(i),
                    "Person " + str(i),
                    "+00" + str(i) + "_1234567890",
                    "2000-12-0" + str(i) + "T23:59:59.999999",
                    0,)
        user.save()
