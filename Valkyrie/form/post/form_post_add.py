from _include.Chimera.Chimera.models import Post, User, Album
from datetime import datetime, timedelta
from django.forms import *


class PostAddForm(Form):
    name = CharField(max_length=50, required=True)
    description = CharField(max_length=255, required=True)
    capacity = IntegerField(max_value=20)

    def process(self, **kwargs):
        if User.objects.filter(id=kwargs.get('user_id')):
            user = User.objects.filter(id=kwargs.pop('user_id')).values()[0]
            chef_id = user.get("chef_id")
            location_id = user.get("location_id")
        else:
            return
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        capacity = self.cleaned_data['capacity']
        post_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
        expire_time = (datetime.utcnow() + timedelta(hours=6)).strftime("%Y-%m-%dT%H:%M:%S.%f")

        album = Album(time=datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f"))
        album.save()

        post = Post(
            chef_id=chef_id,
            location_id=location_id,
            name=name,
            description=description,
            album_id=album.id,
            capacity=capacity,
            post_time=post_time,
            expire_time=expire_time,
        )

        post.save()

        return post.id
