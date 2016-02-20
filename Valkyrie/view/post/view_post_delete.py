from _include.Chimera.Chimera.models import Post, Order, Album
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def post_delete(request, post_id):
    post = Post.objects.filter(pk=post_id)
    if post.count() > 0:
        post = post[0]
    else:
        return HttpResponseRedirect('/posts')

    album = Album.objects.filter(pk=post.album_id)
    if album.count() > 0:
        album = album[0]
    else:
        return HttpResponseRedirect('/posts')

    orders_list = Order.objects.filter(post_id=post.id)
    for order in orders_list:
        try:
            order.delete()
        except StandardError:
            return HttpResponseRedirect('/posts')

    try:
        post.delete()
        album.delete()
    except StandardError:
        return HttpResponseRedirect(reverse('post', args=[post.id, ]))

    return HttpResponseRedirect('/posts')
