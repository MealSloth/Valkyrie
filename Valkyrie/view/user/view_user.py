from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from Valkyrie.models import User


def user(request, user_id):
    temp_user = User.objects.filter(id=user_id)
    result = [
        temp_user.get("id"),
        temp_user.get("user_login_id"),
        temp_user.get("consumer_id"),
        temp_user.get("chef_id"),
        temp_user.get("location_id"),
        temp_user.get("billing_id"),
        temp_user.get("profile_photo_id"),
        temp_user.get("email"),
        temp_user.get("first_name"),
        temp_user.get("last_name"),
        temp_user.get("phone_number"),
        temp_user.get("date_of_birth"),
        temp_user.get("gender"),
    ]
    response = render(request, 'page/user/user.html', Context({"user": result}))
    return HttpResponse(response)
