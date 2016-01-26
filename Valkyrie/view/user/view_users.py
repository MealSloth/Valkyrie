from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from Valkyrie.models import User


def users(request):
    user_list = list(User.objects.all().values())
    response = render(request, 'page/users.html', Context({"user_list": user_list}))
    return HttpResponse(response)
