from _include.Chimera.Chimera.models import Blob
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def blob_delete(request, blob_id):
    blob = Blob.objects.filter(pk=blob_id)
    if blob.count() > 0:
        blob = blob[0]
    else:
        return HttpResponseRedirect('/albums')

    try:
        blob.delete()
        # TODO: Delete GCS blob
    except StandardError:
        return HttpResponseRedirect(reverse('blob', args=[blob.id, ]))

    return HttpResponseRedirect('/albums')
