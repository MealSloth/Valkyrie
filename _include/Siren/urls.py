from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
from Siren import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^consumer/', views.consumer, name='consumer'),
    url(r'^producer/', views.producer, name='producer'),
    url(r'^thanks/(email)/([^/]+)/', views.thanks, name='thanks'),
    url(r'^thanks/(contact)/([^/]+)/', views.thanks, name='thanks'),
) + staticfiles_urlpatterns()
