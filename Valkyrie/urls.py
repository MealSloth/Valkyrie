from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
import views


urlpatterns = patterns(
    '',

    # Home
    url(r'^$', views.home, name='home'),

    # Auth
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^auth-user-add/', views.auth_user_add, name='auth-user-add'),

    # Multi listables
    url(r'^users/', views.users, name='users'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^orders/', views.orders, name='orders'),

    # Single listables
    url(r'^user/([^/]+)/', views.user, name='user'),
    url(r'^post/([^/]+)/', views.post, name='post'),
    url(r'^order/([^/]+)/', views.order, name='order'),
    url(r'^user-login/([^/]+)/', views.user_login, name='user-login'),
    url(r'^consumer/([^/]+)/', views.consumer, name='consumer'),
    url(r'^chef/([^/]+)/', views.chef, name='chef'),
    url(r'^location/([^/]+)/', views.location, name='location'),
    url(r'^billing/([^/]+)/', views.billing, name='billing'),
    url(r'^profile-photo/([^/]+)/', views.profile_photo, name='profile-photo'),

    # Add Forms
    url(r'^user-add/', views.user_add, name='user-add'),
    url(r'^post-add/([^/]+)/', views.post_add, name='post-add'),
    url(r'^blog-post-add/', views.blog_post_add, name='blog-post-add'),

    # Delete Forms
    url(r'^user-delete/([^/]+)/', views.user_delete, name='user-delete'),

    # Tools
    url(r'^tools/', views.tools, name='tools'),

) + staticfiles_urlpatterns()
