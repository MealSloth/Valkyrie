from Valkyrie.form.blob.form_blob_add import BlobAddForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def blob_add(request, album_id):
    if request.method == 'POST':
        form = BlobAddForm(request.POST, request.FILES)
        if form.is_valid():
            blob_id = form.process(album_id)
            return HttpResponseRedirect(reverse('blob', args=[blob_id, ]))
        else:
            return HttpResponseRedirect(reverse('album', args=[album_id, ]))
    else:
        return HttpResponseRedirect(reverse('album', args=[album_id, ]))
