from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Chef
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def chefs(request):
    chefs_view = ChefsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(chefs_view.get_elements()))
    return HttpResponse(response)


class ChefsView(MultiListableView):
    def __init__(self):
        current_chefs_list = Chef.objects.all()

        header = [
            ('ID', 'chef', True),
        ]

        entry = []

        for chef in current_chefs_list:
            entry.append(
                [
                    (chef.id, header[0]),
                ]
            )

        kwargs = {
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
