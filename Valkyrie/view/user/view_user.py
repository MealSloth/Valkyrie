from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from _include.Chimera.models import User


def user(request, user_id):
    current_user = User.objects.filter(id=user_id).values()[0]
    response = render(request, 'page/user/user.html', Context({"user": current_user}))
    return HttpResponse(response)
