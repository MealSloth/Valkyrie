from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Post
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def post(request, post_id):
    post_view = PostView(post_id=post_id)
    response = render(request, 'page/abstract/single-listable.html', Context(post_view.get_elements()))
    return HttpResponse(response)


class PostView(SingleListableView):
    def __init__(self, post_id):
        current_post = Post.objects.filter(pk=post_id)
        if not current_post.values().count() > 0:
            return
        else:
            current_post = current_post[0]

        associated_items = [
                    'Album',
                    'Location',
                ]

        post_delete_button = [
                'fragment/modal/delete-confirmation-modal.html',                            # Modal template
                '',                                                                         # Form template
                '',                                                                         # Form instance
                current_post.id,                                                            # ID parameter for action
                'valkyrie-page-single-listable__post-delete-modal',                         # Modal ID
                '',                                                                         # Modal title text
                'btn btn-danger',                                                           # Button style
                'post-delete',                                                              # Submit action
                '',                                                                         # Submit button text
                'glyphicon glyphicon-trash',                                                # Listable button style
                '',                                                                         # Form CSS class
                '',                                                                         # Form enctype
                'Deleting this post also deletes all of the following associated items:',   # Modal body header
                associated_items,                                                           # Modal body list
                'Are you sure you would like to delete this post?',                         # Modal body footer
            ]

        post_buttons = [post_delete_button, ]

        id = [('Post', current_post.id, post_buttons), ]

        info = [
            ('Name', current_post.name),
            ('Description', current_post.description),
            ('Order Count', current_post.order_count),
            ('Capacity', current_post.capacity),
            ('Post Time', current_post.post_time[:10]),
            ('Expire Time', current_post.expire_time[:10]),
        ]

        widget = [('fragment/widget/single-listable/post-status-widget.html', current_post.post_status), ]

        id_pool = [
            ('Chef ID', current_post.chef_id, 'chef'),
            ('Location ID', current_post.location_id, 'location'),
            ('Album ID', current_post.album_id, 'album'),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'widget': widget,
            'id_pool': id_pool,
        }

        SingleListableView.__init__(
            self, **kwargs
        )
