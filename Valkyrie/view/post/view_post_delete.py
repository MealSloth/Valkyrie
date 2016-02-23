from _include.Chimera.Chimera.settings import PROTOCOL
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from json import dumps
import urllib2


def post_delete(request, post_id):
    try:
        data = {'post_id': post_id}
        data = dumps(data)
        urllib2.urlopen(PROTOCOL + 'api.mealsloth.com/post/delete/', data)
    except urllib2.HTTPError:
        return HttpResponseRedirect(reverse('post', args=[post_id, ]))

    return HttpResponseRedirect('/posts')
