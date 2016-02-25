from _include.Chimera.Chimera.view.post.view_post_modify import post_modify as modify_post
from django.forms import *


class PostEditForm(Form):
    name = CharField(max_length=50, required=True)
    description = CharField(max_length=255, required=True)
    capacity = IntegerField(max_value=20)

    def process(self, post_id):
        post_modify_kwargs = {
            'post_id': post_id,
            'name': self.cleaned_data['name'],
            'description': self.cleaned_data['description'],
            'capacity': self.cleaned_data['capacity'],
        }

        post = modify_post(request=None, **post_modify_kwargs)

        return post
