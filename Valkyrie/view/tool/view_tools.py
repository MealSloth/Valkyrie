from django.http import HttpResponse
from django.shortcuts import render


def tools(request):
    response = render(request, 'page/tool/tools.html')
    return HttpResponse(response)
