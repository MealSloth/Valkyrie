from _include.Chimera.Chimera.models import Post, Order, Album
from _include.Chimera.Chimera.settings import PROTOCOL
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from json import dumps
import urllib2


def post_delete(request, post_id):
    post = Post.objects.filter(pk=post_id)
    if post.count() > 0:
        post = post[0]
    else:
        return HttpResponseRedirect('/posts')

    orders_list = Order.objects.filter(post_id=post.id)
    for order in orders_list:
        try:
            order.delete()
        except StandardError:
            return HttpResponseRedirect('/posts')

    album_id = post.album_id

    try:
        post.delete()
    except StandardError:
        return HttpResponseRedirect(reverse('post', args=[post.id, ]))

    try:
        data = {'album_id': album_id}
        data = dumps(data)
        urllib2.urlopen(PROTOCOL + 'api.mealsloth.com/album/delete/', data)
    except urllib2.HTTPError:
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/posts')
