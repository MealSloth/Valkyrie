from _include.Chimera.Chimera.view.blob.view_blob_upload import blob_upload as upload_blob
from _include.Chimera.Chimera.view.album.view_album_create import album_create as create_album
from _include.Chimera.Chimera.storage_url_suffixes import StorageURLSuffixes
from _include.Chimera.Chimera.models import BlogPost, Author
from datetime import datetime
from base64 import b64encode
from django.forms import *


def authors():
    response = []
    for item in Author.objects.all().values():
        response.append((item.get('id'), item.get('first_name') + ' ' + item.get('last_name')))
    return tuple(response)


class BlogPostAddForm(Form):
    author_id = ChoiceField(choices=authors(), required=True)
    title = CharField(max_length=100, required=True)
    short_description = CharField(max_length=500, required=True)
    long_description = CharField(max_length=10000, required=True, widget=Textarea)
    image = FileField(required=True)

    def process(self):
        author_id = self.cleaned_data['author_id']
        title = self.cleaned_data['title']
        short_description = self.cleaned_data['short_description']
        long_description = self.cleaned_data['long_description']
        image = self.cleaned_data['image']
        post_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")

        album_create_kwargs = {'Please': 'Thank you', }

        album = create_album(request=None, **album_create_kwargs)

        blog_post = BlogPost(
            album_id=album.id,
            author_id=author_id,
            title=title,
            short_description=short_description,
            long_description=long_description,
            post_time=post_time,
        )

        blog_post.save()

        blob_upload_kwargs = {
            'file': b64encode(image.read()),
            'album_id': str(blog_post.album_id),
            'url_suffix': StorageURLSuffixes.get_url_suffix(StorageURLSuffixes.SIREN_BLOG),
        }

        upload_blob(request=None, **blob_upload_kwargs)
