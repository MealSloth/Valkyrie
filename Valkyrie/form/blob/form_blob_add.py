from base64 import b64encode
from django.forms import *
from json import dumps
import urllib2


class BlobAddForm(Form):
    image = FileField(required=True)

    def process(self, album_id):
        image = self.cleaned_data['image']

        data = dumps({
            'file': b64encode(image.read()),
            'album_id': str(album_id),
            'url_suffix': 'siren/blog/',
        })
        try:
            urllib2.urlopen('http://api.mealsloth.com/blog/image/upload/', data)
        except urllib2.HTTPError, error:
            raise ValidationError(error)
