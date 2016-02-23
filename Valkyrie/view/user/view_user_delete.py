from _include.Chimera.Chimera.view.user.view_user_delete import user_delete as chimera_user_delete
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def user_delete(request, user_id):
    user_delete_kwargs = {'user_id': user_id}
    try:
        chimera_user_delete(request=None, **user_delete_kwargs)
    except StandardError:
        return HttpResponseRedirect(reverse('user', args=[user_id, ]))
    return HttpResponseRedirect('/users')
