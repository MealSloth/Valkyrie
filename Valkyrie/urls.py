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
    url(r'^change-password/', views.change_password, name='change-password'),

    # Multi listables
    url(r'^users/', views.users, name='users'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^orders/', views.orders, name='orders'),
    url(r'^user-logins/', views.user_logins, name='user-logins'),
    url(r'^consumers/', views.consumers, name='consumers'),
    url(r'^chefs/', views.chefs, name='chefs'),
    url(r'^locations/', views.locations, name='locations'),
    url(r'^billings/', views.billings, name='billings'),
    url(r'^profile-photos/', views.profile_photos, name='profile-photos'),
    url(r'^albums/', views.albums, name='albums'),
    url(r'^blog-posts/', views.blog_posts, name='blog-posts'),

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
    url(r'^album/([^/]+)/', views.album, name='album'),
    url(r'^blog-post/([^/]+)/', views.blog_post, name='blog-post'),

    # Add Forms
    url(r'^user-add/', views.user_add, name='user-add'),
    url(r'^post-add/([^/]+)/', views.post_add, name='post-add'),
    url(r'^blog-post-add/', views.blog_post_add, name='blog-post-add'),

    # Edit Forms
    url(r'^blog-post-edit/([^/]+)/', views.blog_post_edit, name='blog-post-edit'),

    # Delete Forms
    url(r'^user-delete/([^/]+)/', views.user_delete, name='user-delete'),
    url(r'^post-delete/([^/]+)/', views.post_delete, name='post-delete'),

    # Tools
    url(r'^tools/', views.tools, name='tools'),

) + staticfiles_urlpatterns()
