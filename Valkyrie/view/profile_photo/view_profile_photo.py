from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import ProfilePhoto
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def profile_photo(request, profile_photo_id):
    profile_photo_view = ProfilePhotoView(profile_photo_id=profile_photo_id)
    response = render(request, 'page/abstract/single-listable.html', Context(profile_photo_view.get_elements()))
    return HttpResponse(response)


class ProfilePhotoView(SingleListableView):
    def __init__(self, profile_photo_id):
        current_profile_photo = ProfilePhoto.objects.filter(pk=profile_photo_id)
        if not current_profile_photo.values().count() > 0:
            return
        else:
            current_profile_photo = current_profile_photo[0]

        id = [current_profile_photo.id, ]

        kwargs = {
            'id': id,
        }

        SingleListableView.__init__(self, **kwargs)
