from _include.Chimera.Chimera.models import User, Post, Album, Blob, ProfilePhoto
from Valkyrie.view.abstract.view_single_listable import SingleListableView
from Valkyrie.form.post.form_post_add import PostAddForm
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
        current_user = User.objects.filter(pk=user_id)
        if not current_user.values().count() > 0:
            return
        else:
            current_user = current_user[0]

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

        user_delete_button = [
                'fragment/modal/delete-confirmation/user-delete-confirmation-modal.html',   # Modal template
                '',                                                                         # Form template
                '',                                                                         # Form instance
                current_user.id,                                                            # ID parameter for action
                'valkyrie-page-single-listable__user-delete-modal',                         # Modal ID
                '',                                                                         # Modal title text
                '',                                                                         # Button style
                '',                                                                         # Form action
                '',                                                                         # Submit button text
                'glyphicon glyphicon-trash',                                                # Listable button style
                '',                                                                         # Form CSS class
                '',                                                                         # Form enctype
            ]

        user_buttons = [user_delete_button, ]

        id = [('User', current_user.id, user_buttons), ]

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

        post_add_button = [
                'fragment/modal/form/form-modal.html',              # Modal template
                'fragment/modal/form/add-form/post-add-form.html',  # Form template
                PostAddForm(),                                      # Form instance
                current_user.id,                                    # ID parameter for action
                'valkyrie-page-single-listable__post-add-modal',    # Modal ID
                'Add Post',                                         # Modal title text
                'btn btn-primary',                                  # Button style
                'post-add',                                         # Form action
                'Add Post',                                         # Submit button text
                'glyphicon glyphicon-plus',                         # Listable button style
                'valkyrie-fragment-form__section-form',             # Form CSS class
                '',                                                 # Form enctype
            ]

        post_buttons = [post_add_button, ]

        listable = [
            ('Email Addresses', email_addresses),
            ('Phone Numbers', phone_numbers),
            ('Posts', post_array, 'post', 'status', post_buttons),
        ]

        # modal = [(
        #     'fragment/modal/delete-confirmation/user-delete-confirmation-modal.html',
        #     'valkyrie-page-single-listable__user-delete-modal',
        #     'glyphicon glyphicon-trash',
        #     current_user.id,
        # )]

        kwargs = {
            'image': image,
            'id': id,
            'info': info,
            'widget': widget,
            'id_pool': id_pool,
            'listable': listable,
            # 'modal': modal,
        }

        SingleListableView.__init__(
            self, **kwargs
        )
