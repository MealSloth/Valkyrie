from _include.Chimera.Chimera.storage_url_suffixes import StorageURLSuffixes
from base64 import b64encode
from django.forms import *
from json import dumps
import urllib2


def url_suffixes():
    response = []
    dictionary = StorageURLSuffixes.get_url_suffixes()
    for key in dictionary:
        response.append((key, dictionary.get(key)))
    return tuple(response)


class BlobAddForm(Form):
    url_suffix = ChoiceField(choices=url_suffixes(), required=True)
    image = FileField(required=True)

    def process(self, album_id):
        image = self.cleaned_data['image']
        url_suffix = self.cleaned_data['url_suffix']

        data = dumps({
            'file': b64encode(image.read()),
            'album_id': str(album_id),
            'url_suffix': url_suffix,
        })
        try:
            urllib2.urlopen('http://api.mealsloth.com/blob/upload/', data)
        except urllib2.HTTPError, error:
            raise ValidationError(error)
