from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import UserLogin, User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context


def user_login(request, user_login_id):
    user_view = UserLoginView(user_login_id=user_login_id)
    response = render(request, 'page/abstract/single-listable.html', Context(user_view.get_elements()))
    return HttpResponse(response)


class UserLoginView(SingleListableView):
    def __init__(self, user_login_id):
        current_user_login = UserLogin.objects.filter(pk=user_login_id)
        if not current_user_login.values().count() > 0:
            return
        else:
            current_user_login = current_user_login[0]

        id = [current_user_login.id, ]

        info = []

        associated_user = User.objects.filter(pk=current_user_login.user_id)

        if associated_user.values().count() > 0:
            associated_user = associated_user[0]
            info = [('Associated User', associated_user.first_name + ' ' + associated_user.last_name), ]

        info.append(('Username', current_user_login.username))
        info.append(('Access Level', current_user_login.get_access_level_display()))

        id_pool = [
            ('User ID', current_user_login.user_id, 'user'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(
            self, **kwargs
        )
