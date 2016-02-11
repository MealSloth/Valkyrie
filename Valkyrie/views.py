from view.home import view_home
from view.order import view_order, view_orders
from view.post import view_post, view_posts, view_post_add
from view.user import view_user, view_users, view_user_add, view_user_delete
from view.tool import view_tools, view_blog_post_add, view_test_photo_upload, view_test_photo_view
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


# tools

@login_required
def tools(request):
    return view_tools.tools(request)


@login_required
def blog_post_add(request):
    return view_blog_post_add.blog_post_add(request)


@login_required
def test_photo_upload(request):
    return view_test_photo_upload.test_photo_upload(request)


@login_required
def test_photo_view(request):
    return view_test_photo_view.test_photo_view(request)
