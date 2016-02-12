from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^auth-user-add/', views.auth_user_add, name='auth-user-add'),
    url(r'^users/', views.users, name='users'),
    url(r'^posts/', views.posts, name='posts'),
    url(r'^orders/', views.orders, name='orders'),
    url(r'^tools/', views.tools, name='tools'),
    url(r'^user/([^/]+)/', views.user, name='user'),
    url(r'^user-add/', views.user_add, name='user-add'),
    url(r'^user-delete/([^/]+)/', views.user_delete, name='user-delete'),
    url(r'^post/([^/]+)/', views.post, name='post'),
    url(r'^post-add/([^/]+)/', views.post_add, name='post-add'),
    url(r'^order/([^/]+)/', views.order, name='order'),
    url(r'^blog-post-add/', views.blog_post_add, name='blog-post-add'),
    url(r'^blob-image-upload/', views.blob_image_upload, name='blob-image-upload'),
    url(r'^blob-image-view/([^/]+)/', views.blob_image_view, name='blob-image-view'),
) + staticfiles_urlpatterns()
