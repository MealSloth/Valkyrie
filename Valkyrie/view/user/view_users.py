from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import User
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def users(request):
    users_view = UsersView()
    response = render(request, 'page/abstract/multi-listable.html', Context(users_view.get_elements()))
    return HttpResponse(response)


class UsersView(MultiListableView):
    def __init__(self):
        current_users_list = User.objects.all().order_by('join_date')

        header = [
            ('ID', 'user', True),           # ('Column Title', 'URL parameter (if linked)', Boolean display on mobile)
            ('Name', '', False),
            ('Gender', '', False),
            ('Email', '', True),
            ('Phone Number', '', False),
            ('Date of Birth', '', False),
        ]

        entry = []

        for user in current_users_list:
            entry.append(
                [
                    (user.id, header[0]),                                   # (Entry, Corresponding header[] tuple)
                    (user.first_name + ' ' + user.last_name, header[1]),
                    (user.get_gender_display(), header[2]),
                    (user.email, header[3]),
                    (user.phone_number, header[4]),
                    (user.date_of_birth, header[5]),
                ]
            )

        kwargs = {
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
