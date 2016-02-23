from _include.Chimera.Chimera.view.blob.view_blob_delete import blob_delete as chimera_blob_delete
from django.http import HttpResponseRedirect


def blob_delete(request, blob_id):
    blob_delete_kwargs = {'blob_id': blob_id}
    chimera_blob_delete(request=None, **blob_delete_kwargs)
    return HttpResponseRedirect('/albums')
