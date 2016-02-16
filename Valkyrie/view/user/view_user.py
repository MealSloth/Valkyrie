from _include.Chimera.Chimera.models import User, Post, Album, Blob, ProfilePhoto
from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.settings import GCS_URL
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def user(request, user_id):
    user_view = UserView(user_id=user_id)
    response = render(request, 'page/abstract/single-listable.html', Context(user_view.get_elements()))
    return HttpResponse(response)


class UserView(SingleListableView):
    def __init__(self, user_id):
        current_user = User.objects.get(pk=user_id)

        gcs_id = Blob.objects.filter(
            album_id=Album.objects.get(
                pk=ProfilePhoto.objects.get(
                    pk=current_user.profile_photo_id).album_id
            )
        ).values()

        if gcs_id.count() > 0:
            gcs_id = gcs_id.get('gcs_id')
            image = [GCS_URL + gcs_id, ]
        else:
            image = []

        id = [current_user.id, ]

        info = [
            ('Name', current_user.first_name + ' ' + current_user.last_name),
            ('Gender', current_user.get_gender_display()),
            ('Date of Birth', current_user.date_of_birth[:10]),
            ('Join Date', current_user.join_date[:10]),
        ]

        widget = []

        id_pool = [
            ('User Login ID', current_user.user_login_id, 'user-login'),
            ('Consumer ID', current_user.consumer_id, 'consumer'),
            ('Chef ID', current_user.chef_id, 'chef'),
            ('Location ID', current_user.location_id, 'location'),
            ('Billing ID', current_user.billing_id, 'billing'),
            ('Profile Photo ID', current_user.profile_photo_id, 'profile-photo'),
        ]

        email_addresses = [current_user.email, ]
        phone_numbers = [current_user.phone_number, ]
        posts = Post.objects.filter(chef_id=current_user.chef_id)

        post_array = []

        for i in range(0, posts.count()):
            post_array.append([posts[i].id, posts[i].post_status, posts[i].get_post_status_display()])

        listable = [
            ('Email Addresses', email_addresses),
            ('Phone Numbers', phone_numbers),
            ('Posts', post_array, 'post', 'true'),
        ]

        SingleListableView.__init__(
            self, image=image, id=id, info=info, id_pool=id_pool, widget=widget, listable=listable
        )
