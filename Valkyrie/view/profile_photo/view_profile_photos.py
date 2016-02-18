from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import ProfilePhoto
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def profile_photos(request):
    profile_photos_view = ProfilePhotosView()
    response = render(request, 'page/abstract/multi-listable.html', Context(profile_photos_view.get_elements()))
    return HttpResponse(response)


class ProfilePhotosView(MultiListableView):
    def __init__(self):
        current_profile_photos_list = ProfilePhoto.objects.all()

        header = [
            ('ID', 'profile-photo', True),
        ]

        entry = []

        for profile_photo in current_profile_photos_list:
            entry.append(
                [
                    (profile_photo.id, header[0]),
                ]
            )

        kwargs = {
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
