from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from Valkyrie.models import Post


def post(request, post_id):
    current_post = Post.objects.filter(id=post_id).values()[0]
    response = render(request, 'page/post/post.html', Context({"post": current_post}))
    return HttpResponse(response)
