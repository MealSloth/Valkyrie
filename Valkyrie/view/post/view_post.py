from Valkyrie.view.abstract.view_single_listable import SingleListableView
from Valkyrie.form.order.form_order_add import OrderAddForm
from Valkyrie.form.post.form_post_edit import PostEditForm
from _include.Chimera.Chimera.models import Post, Order
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

        post_edit_button = [
                'fragment/modal/form/form-modal.html',                          # Modal template
                'fragment/modal/form/add-form/post-add-edit-form.html',         # Form template
                PostEditForm({                                                  # Form instance
                    'name': current_post.name,
                    'description': current_post.description,
                    'capacity': current_post.capacity,
                }),
                current_post.id,                                                # ID parameter for action
                'valkyrie-page-single-listable__post-edit-modal',               # Modal ID
                'Edit Post',                                                    # Modal title text
                'btn btn-primary',                                              # Button style
                'post-edit',                                                    # Form action
                'Save Edit',                                                    # Submit button text
                'glyphicon glyphicon-pencil',                                   # Listable button style
                'valkyrie-fragment-form__section-form',                         # Form CSS class
                '',                                                             # Form enctype
            ]

        associated_items = [
                    'Album',
                    'Order',
                ]

        post_delete_button = [
                'fragment/modal/delete-confirmation-modal.html',                            # Modal template
                '',                                                                         # Form template
                '',                                                                         # Form instance
                current_post.id,                                                            # ID parameter for action
                'valkyrie-page-single-listable__post-delete-modal',                         # Modal ID
                'Delete Post',                                                              # Modal title text
                'btn btn-danger',                                                           # Button style
                'post-delete',                                                              # Submit action
                'Delete Post',                                                              # Submit button text
                'glyphicon glyphicon-trash',                                                # Listable button style
                '',                                                                         # Form CSS class
                '',                                                                         # Form enctype
                'Deleting this post also deletes all of the following associated items:',   # Modal body header
                associated_items,                                                           # Modal body list
                'Are you sure you would like to delete this post?',                         # Modal body footer
            ]

        post_buttons = [post_edit_button, post_delete_button, ]

        id = [('Post', current_post.id, post_buttons), ]

        info = [
            ('Name', current_post.name),
            ('Description', current_post.description),
            ('Order Count', current_post.order_count),
            ('Capacity', current_post.capacity),
            ('Post Time', current_post.post_time[5:16].replace("T", " ")),
            ('Expire Time', current_post.expire_time[5:16].replace("T", " ")),
        ]

        widget = [('fragment/widget/single-listable/post-status-widget.html', current_post.post_status), ]

        id_pool = [
            ('Chef ID', current_post.chef_id, 'chef'),
            ('Location ID', current_post.location_id, 'location'),
            ('Album ID', current_post.album_id, 'album'),
        ]

        orders = Order.objects.filter(post_id=current_post.id)

        order_array = []

        for i in range(0, orders.count()):
            order_array.append([orders[i].id, orders[i].order_status, orders[i].get_order_status_display()])

        order_add_button = [
                'fragment/modal/form/form-modal.html',                  # Modal template
                'fragment/modal/form/add-form/order-add-form.html',     # Form template
                OrderAddForm(),                                         # Form instance
                current_post.id,                                        # ID parameter for action
                'valkyrie-page-single-listable__order-add-modal',       # Modal ID
                'Add Test Order',                                       # Modal title text
                'btn btn-primary',                                      # Button style
                'order-add',                                            # Form action
                'Add Test Order',                                       # Submit button text
                'glyphicon glyphicon-plus',                             # Header button style
                'valkyrie-fragment-form__section-form',                 # Form CSS class
                '',                                                     # Form enctype
            ]

        order_buttons = [order_add_button, ]

        listable = [
            ('Orders', order_array, 'order', 'status', order_buttons),
        ]

        kwargs = {
            'id': id,
            'info': info,
            'widget': widget,
            'id_pool': id_pool,
            'listable': listable,
        }

        SingleListableView.__init__(
            self, **kwargs
        )
