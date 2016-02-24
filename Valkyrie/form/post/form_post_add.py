from _include.Chimera.Chimera.view.post.view_post_create import post_create as create_post
from _include.Chimera.Chimera.models import User
from django.forms import *


class PostAddForm(Form):
    name = CharField(max_length=50, required=True)
    description = CharField(max_length=255, required=True)
    capacity = IntegerField(max_value=20)

    def process(self, user_id):
        user = User.objects.get(pk=user_id)
        post_create_kwargs = {
            'chef_id': user.chef_id,
            'name': self.cleaned_data['name'],
            'description': self.cleaned_data['description'],
            'capacity': self.cleaned_data['capacity'],
        }

        post = create_post(request=None, **post_create_kwargs)

        return post
