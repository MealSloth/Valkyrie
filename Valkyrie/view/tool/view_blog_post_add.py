from Valkyrie.form.tool.form_blog_post_add import BlogPostAddForm
from django.http import HttpResponse, HttpResponseRedirect
from _include.Chimera.Chimera.settings import PROTOCOL
from django.shortcuts import render
from django.template import Context


def blog_post_add(request):
    error = ''
    if request.method == 'POST':
        form = BlogPostAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.process()
            return HttpResponseRedirect(PROTOCOL + 'test.mealsloth.com/blog/')
        else:
            error = 'Invalid form'

    return HttpResponse(render(
        request,
        'page/tool/blog-post-add.html',
        Context({'form': BlogPostAddForm(), 'error': error})
    ))
