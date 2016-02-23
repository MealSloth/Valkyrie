from _include.Chimera.Chimera.settings import PROTOCOL
from _include.Chimera.Chimera.models import Blob
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from json import dumps
import urllib2


def blob_delete(request, blob_id):
    blob = Blob.objects.filter(pk=blob_id)
    if blob.count() > 0:
        blob = blob[0]
    else:
        return HttpResponseRedirect(reverse('blob', args=[blob_id, ]))
    try:
        data = {'blob_id': blob.id}
        data = dumps(data)
        urllib2.urlopen(PROTOCOL + 'api.mealsloth.com/blob/delete/', data)
        return HttpResponseRedirect('/albums')
    except urllib2.HTTPError:
        return HttpResponseRedirect(reverse('blob', args=[blob_id, ]))
