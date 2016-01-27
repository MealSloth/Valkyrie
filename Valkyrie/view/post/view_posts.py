from django.http import HttpResponse
from django.shortcuts import render


def posts(request):
    response = render(request, 'page/post/posts.html')
    return HttpResponse(response)
