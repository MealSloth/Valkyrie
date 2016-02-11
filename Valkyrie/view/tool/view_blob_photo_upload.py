from _include.Hydra.Hydra.form.photo.form_blob_photo_upload import BlobPhotoUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
import urllib2
import urllib


def blob_photo_upload(request):
    if request.method == 'POST':
        form = BlobPhotoUploadForm(request.POST, request.FILES)
        form.set_origin('Valkyrie')
        if form.is_valid():
            response = urllib2.urlopen('http://blob.mealsloth.com/blob-photo-upload/', urllib.urlencode(form))
            result = response.read()
            print(result)
            return HttpResponseRedirect('/tools')
        else:
            return HttpResponse("Invalid form")
    else:
        return render(request, 'page/tool/blob-photo-upload.html', Context({'form': BlobPhotoUploadForm()}))
