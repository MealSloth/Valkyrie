from _include.Chimera.Chimera.models import BlogPost, Author
from datetime import datetime
from json import dumps, loads
from base64 import b64encode
from django.forms import *
import urllib2


def authors():
    response = []
    for item in Author.objects.all().values():
        response.append((item.get('id'), item.get('first_name') + ' ' + item.get('last_name')))
    return tuple(response)


class BlogPostAddForm(Form):
    author_id = ChoiceField(choices=authors(), required=True)
    title = CharField(max_length=100, required=True)
    short_description = CharField(max_length=500, required=True)
    long_description = CharField(max_length=10000, required=True)
    image = FileField(required=True)

    def process(self):
        author_id = self.cleaned_data['author_id']
        title = self.cleaned_data['title']
        short_description = self.cleaned_data['short_description']
        long_description = self.cleaned_data['long_description']
        image = self.cleaned_data['image']
        post_time = datetime.utcnow()

        blog_post = BlogPost(
            author_id=author_id,
            title=title,
            short_description=short_description,
            long_description=long_description,
            post_time=post_time,
        )

        blog_post.save()

        data = dumps({'file': b64encode(image.read()), 'album_id': str(blog_post.album_id), })
        re = loads(urllib2.urlopen('http://api.mealsloth.com/blog-image-upload/', data))
        if re['result'] != 1000:
            blog_post.delete()
