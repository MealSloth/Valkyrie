from _include.Hydra.Hydra.form.image.form_blob_image_upload import BlobImageUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
from json import dumps, loads
from base64 import b64encode
import urllib2
import imghdr


def blob_image_upload(request):
    if request.method == 'POST':
        form = BlobImageUploadForm(request.POST, request.FILES)
        request.FILES['file'].seek(0)
        if form.is_valid():
            data = dumps({'file': b64encode(request.FILES['file'].read())})
            re = loads(urllib2.urlopen('http://api.mealsloth.com/blob-image-upload/', data))
            if re['result'] == 1000:
                return HttpResponseRedirect('/tools')
            else:
                return HttpResponseRedirect('/')
        else:
            response = render(request, 'page/tool/blob-image-upload.html', Context({'form': BlobImageUploadForm()}))
            return HttpResponse(response)
    else:
        response = render(request, 'page/tool/blob-image-upload.html', Context({'form': BlobImageUploadForm()}))
        return HttpResponse(response)
