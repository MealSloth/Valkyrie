from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import Location
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def locations(request):
    locations_view = LocationsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(locations_view.get_elements()))
    return HttpResponse(response)


class LocationsView(MultiListableView):
    def __init__(self):
        current_locations_list = Location.objects.all()

        header = [
            ('ID', 'location', True),
        ]

        entry = []

        for location in current_locations_list:
            entry.append(
                [
                    (location.id, header[0]),
                ]
            )

        kwargs = {
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
