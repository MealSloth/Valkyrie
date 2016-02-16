from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import ProfilePhoto, User
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

        id = [('Profile Photo', current_profile_photo.id), ]

        associated_user = User.objects.filter(pk=current_profile_photo.user_id)

        if associated_user.values().count() > 0:
            associated_user = associated_user[0]
            info = [('Associated User', associated_user.first_name + ' ' + associated_user.last_name), ]
        else:
            info = []

        id_pool = [
            ('Album ID', current_profile_photo.album_id, 'album'),
            ('User ID', current_profile_photo.user_id, 'user'),
            ('Consumer ID', current_profile_photo.consumer_id, 'consumer'),
            ('Chef ID', current_profile_photo.chef_id, 'chef'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(self, **kwargs)
