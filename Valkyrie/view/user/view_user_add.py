from django.http import HttpResponseRedirect
from django.shortcuts import render
from Valkyrie.form.user.form_user_add import UserAddForm


def user_add(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.process()
            return HttpResponseRedirect('/users')
    else:
        form = UserAddForm()

    return render(request, 'page/user/user-add.html', {'form': form})
