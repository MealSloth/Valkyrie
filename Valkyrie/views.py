from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from Valkyrie.models import User


def home(request):
    response = render(request, 'page/home.html')
    return HttpResponse(response)


def users(request):
    user_list = list(User.objects.all().values())
    response = render(request, 'page/users.html', Context({"user_list": user_list}))
    return HttpResponse(response)


def posts(request):
    response = render(request, 'page/posts.html')
    return HttpResponse(response)


def orders(request):
    response = render(request, 'page/orders.html')
    return HttpResponse(response)


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
    response = render(request, 'page/user.html', Context({"user": result}))
    return HttpResponse(response)


# Not to be used right now
# def generate_users():
#     for i in range(21, 32):
#         temp_user = User(i, i, i, i, i, i, i,
#                          "TestPerson" + str(i) + "@gmail.com",
#                          "Test",
#                          "Person " + str(i),
#                          "+0" + str(i) + "_1234567890",
#                          "2000-12-" + str(i) + "T23:59:59.999999",
#                          0, )
#         temp_user.save()
