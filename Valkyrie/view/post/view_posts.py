from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from Valkyrie.models import Post


def posts(request):
    post_list = list(Post.objects.all().order_by('status').values())
    response = render(request, 'page/post/posts.html', Context({"post_list": post_list}))
    return HttpResponse(response)
