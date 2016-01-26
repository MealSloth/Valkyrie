from django.http import HttpResponse
from django.shortcuts import render


def posts(request):
    response = render(request, 'page/posts.html')
    return HttpResponse(response)
