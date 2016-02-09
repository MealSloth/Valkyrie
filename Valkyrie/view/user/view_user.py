from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from _include.Chimera.Chimera.models import User, Post


def user(request, user_id):
    current_user = User.objects.filter(id=user_id).values()[0]
    posts = Post.objects.filter(chef_id=current_user.get('chef_id')).values()
    response = render(request, 'page/user/user.html', Context({'user': current_user, 'posts': posts}))
    return HttpResponse(response)
