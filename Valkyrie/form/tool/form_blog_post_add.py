from django.forms import *
from _include.Siren.Siren.models import BlogPost, Author
from datetime import datetime


def authors():
    response = []
    for item in Author.objects.using('siren').all().values():
        response.append((item.get('id'), item.get('first_name') + ' ' + item.get('last_name')))
    return tuple(response)


class BlogPostAddForm(Form):
    author_id = ChoiceField(choices=authors(), required=True)
    title = CharField(max_length=100, required=True)
    short_description = CharField(max_length=500, required=True)
    long_description = CharField(max_length=10000, required=True)

    def process(self):
        author_id = self.cleaned_data['author_id']
        title = self.cleaned_data['title']
        short_description = self.cleaned_data['short_description']
        long_description = self.cleaned_data['long_description']
        post_time = datetime.utcnow()

        blog_post = BlogPost(
            author_id=author_id,
            title=title,
            short_description=short_description,
            long_description=long_description,
            post_time=post_time,
        )

        print(blog_post)

        blog_post.save(using='siren')
