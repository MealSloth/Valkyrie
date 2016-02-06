from django.contrib.auth.models import User
from django.forms import *


class AuthUserAddForm(Form):
    first_name = CharField(max_length=30, required=True)
    last_name = CharField(max_length=30, required=True)
    username = CharField(max_length=30, required=True)
    password = CharField(required=True, widget=PasswordInput())
    password_confirm = CharField(required=True, widget=PasswordInput())

    def process(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password == password_confirm:
            pass
        else:
            return

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

        user.set_password(password)

        user.save()
