from _include.Hydra.Hydra.form.photo.form_blob_photo_upload import BlobPhotoUploadForm
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.template import Context
import urllib2
import urllib


def blob_photo_upload(request):
    if request.method == 'POST':
        form = BlobPhotoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                with open(form.file) as image:
                    response = urllib.urlopen('http://api.mealsloth.com/blob-photo-upload/',
                                              urllib.urlencode({'file': image, }))
                    result = response.read()
                    print(result)
                    return HttpResponseRedirect('/tools')
            except IOError:
                return HttpResponseRedirect('/users')
            # response = urllib2.urlopen('http://blob.mealsloth.com/blob-photo-upload/', urllib.urlencode(form))
            # result = response.read()
            # print(result)
            # return HttpResponseRedirect('/tools')
        else:
            return HttpResponse("Invalid form")
    else:
        return render(request, 'page/tool/blob-photo-upload.html', Context({'form': BlobPhotoUploadForm()}))
