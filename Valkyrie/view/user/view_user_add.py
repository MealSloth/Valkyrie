from django.http import HttpResponse
from django.shortcuts import render


def user_add(request):
    response = render(request, 'page/user-add.html')
    return HttpResponse(response)
