from django.http import HttpResponseRedirect

from Valkyrie.form.blog_post.form_blog_post_add import BlogPostAddForm
from _include.Chimera.Chimera.settings import PROTOCOL


def blog_post_add(request):
    if request.method == 'POST':
        form = BlogPostAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.process()
            return HttpResponseRedirect(PROTOCOL + 'mealsloth.com/blog/')

    return HttpResponseRedirect('/blogs')
