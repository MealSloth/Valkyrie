from Valkyrie.view.abstract.view_multi_listable import MultiListableView
from _include.Chimera.Chimera.models import BlogPost, Author
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def blog_posts(request):
    blog_posts_view = BlogPostsView()
    response = render(request, 'page/abstract/multi-listable.html', Context(blog_posts_view.get_elements()))
    return HttpResponse(response)


class BlogPostsView(MultiListableView):
    def __init__(self):
        current_blog_posts_list = BlogPost.objects.all()

        title = ["Blog Posts", ]

        header = [
            ('ID', 'blog-post', True),
            ('Title', '', True),
            ('Author', '', True),
            ('Short Description', '', False),
            ('Long Description', '', False),
        ]

        entry = []

        for blog_post in current_blog_posts_list:
            author = Author.objects.get(pk=blog_post.author_id)
            entry.append(
                [
                    (blog_post.id, header[0]),
                    (blog_post.title, header[1]),
                    (author.first_name + ' ' + author.last_name, header[2]),
                    (blog_post.short_description[:30] + ' ...', header[3]),
                    (blog_post.long_description[:40] + ' ...', header[4]),
                ]
            )

        kwargs = {
            'title': title,
            'header': header,
            'entry': entry,
        }

        MultiListableView.__init__(self, **kwargs)
