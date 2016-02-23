from _include.Chimera.Chimera.models import User, UserLogin, Consumer, Chef, Location, Billing, Album, ProfilePhoto
from _include.Chimera.Chimera.settings import PROTOCOL
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from json import dumps
import urllib2


def user_delete(request, user_id):
    user = User.objects.get(pk=user_id)

    if not user:
        return HttpResponseRedirect(reverse('user', user_id))

    try:
        user_login = UserLogin.objects.get(pk=user.user_login_id)
    except UserLogin.DoesNotExist:
        user_login = None

    try:
        location = Location.objects.get(pk=user.location_id)
    except Location.DoesNotExist:
        location = None

    try:
        consumer = Consumer.objects.get(pk=user.consumer_id)
    except Consumer.DoesNotExist:
        consumer = None

    try:
        chef = Chef.objects.get(pk=user.chef_id)
    except Chef.DoesNotExist:
        chef = None

    try:
        billing = Billing.objects.get(pk=user.billing_id)
    except Billing.DoesNotExist:
        billing = None

    try:
        profile_photo = ProfilePhoto.objects.get(pk=user.profile_photo_id)
    except ProfilePhoto.DoesNotExist:
        profile_photo = None

    if profile_photo:
        try:
            album = Album.objects.get(pk=profile_photo.album_id)
        except Album.DoesNotExist:
            album = None
    else:
        album = None

    if profile_photo:
        profile_photo.delete()

    if album:
        try:
            data = {'album_id': album.id}
            data = dumps(data)
            urllib2.urlopen(PROTOCOL + 'api.mealsloth.com/album/delete/', data)
        except urllib2.HTTPError:
            return

    if billing:
        billing.delete()

    if consumer:
        consumer.delete()

    if chef:
        chef.delete()

    if location:
        location.delete()

    if user_login:
        user_login.delete()

    if user:
        user.delete()

    return HttpResponseRedirect('/users')
