from _include.Chimera.Chimera.view.post.view_post_delete import post_delete as chimera_post_delete
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def post_delete(request, post_id):
    post_delete_kwargs = {'post_id': post_id}
    try:
        chimera_post_delete(request=None, **post_delete_kwargs)
    except StandardError:
        HttpResponseRedirect(reverse('post', args=[post_id, ]))
    return HttpResponseRedirect('/posts')
