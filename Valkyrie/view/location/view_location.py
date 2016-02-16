from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Location
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def location(request, location_id):
    location_view = LocationView(location_id=location_id)
    response = render(request, 'page/abstract/single-listable.html', Context(location_view.get_elements()))
    return HttpResponse(response)


class LocationView(SingleListableView):
    def __init__(self, location_id):
        current_location = Location.objects.filter(pk=location_id)
        if not current_location.values().count() > 0:
            return
        else:
            current_location = current_location[0]

        id = [current_location.id, ]

        kwargs = {
            'id': id,
        }

        SingleListableView.__init__(self, **kwargs)
