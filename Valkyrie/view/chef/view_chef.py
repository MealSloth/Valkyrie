from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Chef
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def chef(request, chef_id):
    chef_view = ChefView(chef_id=chef_id)
    response = render(request, 'page/abstract/single-listable.html', Context(chef_view.get_elements()))
    return HttpResponse(response)


class ChefView(SingleListableView):
    def __init__(self, chef_id):
        current_chef = Chef.objects.filter(pk=chef_id)
        if not current_chef.values().count() > 0:
            return
        else:
            current_chef = current_chef[0]

        id = [current_chef.id, ]

        kwargs = {
            'id': id,
        }

        SingleListableView.__init__(self, **kwargs)
