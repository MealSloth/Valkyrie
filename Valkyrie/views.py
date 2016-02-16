from view.home import view_home
from view.album import view_album
from view.order import view_order, view_orders
from view.post import view_post, view_posts, view_post_add
from view.user import view_user, view_users, view_user_add, view_user_delete, view_user_login
from view.consumer import view_consumer
from view.chef import view_chef
from view.location import view_location
from view.billing import view_billing
from view.profile_photo import view_profile_photo
from view.tool import view_tools, view_blog_post_add
from view.auth import view_login, view_logout, view_auth_user_add

from django.contrib.auth.decorators import login_required


# home

@login_required
def home(request):
    return view_home.home(request)


# auth

def login(request):
    return view_login.login(request)


def logout(request):
    return view_logout.logout(request)


@login_required
def auth_user_add(request):
    return view_auth_user_add.auth_user_add(request)


# user

@login_required
def users(request):
    return view_users.users(request)


@login_required
def user(request, user_id):
    return view_user.user(request, user_id)


@login_required
def user_add(request):
    return view_user_add.user_add(request)


@login_required
def user_delete(request, user_id):
    return view_user_delete.user_delete(request, user_id)


# user_login

@login_required
def user_login(request, user_login_id):
    return view_user_login.user_login(request, user_login_id)


# consumer

@login_required
def consumer(request, consumer_id):
    return view_consumer.consumer(request, consumer_id)


# chef

@login_required
def chef(request, chef_id):
    return view_chef.chef(request, chef_id)


# location

@login_required
def location(request, location_id):
    return view_location.location(request, location_id)


# billing

@login_required
def billing(request, billing_id):
    return view_billing.billing(request, billing_id)


# profile_photo

@login_required
def profile_photo(request, profile_photo_id):
    return view_profile_photo.profile_photo(request, profile_photo_id)


# post

@login_required
def posts(request):
    return view_posts.posts(request)


@login_required
def post(request, post_id):
    return view_post.post(request, post_id)


@login_required
def post_add(request, user_id):
    return view_post_add.post_add(request, user_id)


# order

@login_required
def orders(request):
    return view_orders.orders(request)


@login_required
def order(request, order_id):
    return view_order.order(request, order_id)


# album

@login_required
def album(request, album_id):
    return view_album.album(request, album_id)


# tools

@login_required
def tools(request):
    return view_tools.tools(request)


@login_required
def blog_post_add(request):
    return view_blog_post_add.blog_post_add(request)
