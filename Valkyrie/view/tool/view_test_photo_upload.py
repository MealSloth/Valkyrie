from _include.Chimera.lib.google.storage.google_cloud import GoogleCloudStorage
from Valkyrie.form.tool.form_test_photo_upload import TestPhotoUploadForm
from _include.Chimera.Chimera.models import Blob, Album
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context


def test_photo_upload(request):
    if request.method == 'POST':
        form = TestPhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            gcs = GoogleCloudStorage()

            album = Album()
            album.save()

            blob = Blob(
                album_id=album.id,
            )

            blob.save()
            blob.gcs_id = gcs.save('user/profile-photo/' + str(blob.id), request.FILES['file'])
            print(blob.gcs_id)
            blob.save()

            return HttpResponseRedirect('/tools')
        else:
            return HttpResponse("Invalid form")
    else:
        return render(request, 'page/tool/test-photo-upload.html', Context({'form': TestPhotoUploadForm()}))
