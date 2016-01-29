from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from _include.Chimera.models import User


def users(request):
    user_list = list(User.objects.all().order_by('join_date').values())
    response = render(request, 'page/user/users.html', Context({"user_list": user_list}))
    return HttpResponse(response)
