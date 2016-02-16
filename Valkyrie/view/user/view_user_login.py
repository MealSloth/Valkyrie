from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import UserLogin
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context


def user_login(request, user_login_id):
    user_view = UserLoginView(user_login_id=user_login_id)
    response = render(request, 'page/abstract/single-listable.html', Context(user_view.get_elements()))
    return HttpResponse(response)


class UserLoginView(SingleListableView):
    def __init__(self, user_login_id):
        current_user_login = UserLogin.objects.get(pk=user_login_id)
