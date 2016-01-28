from django.http import HttpResponseRedirect
from django.shortcuts import render
from Valkyrie.form.post.form_post_add import PostAddForm


def post_add(request, user_id):
    if request.method == 'POST':
        keys = {'user_id': user_id}
        form = PostAddForm(request.POST)
        if form.is_valid():
            form.process(**keys)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostAddForm()

    return render(request, 'page/post/post-add.html', {'form': form, 'user_id': user_id})
