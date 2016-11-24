from django.conf.urls import url

from . import views
 
urlpatterns = [

    # ex: /webD/
    url(r'^login\.html$', views.login, name='login'),

    # ex: /webD/logout/
    url(r'^signup\.html$', views.signup, name='logout'),

    # ex: /webD/home/
    url(r'^home\.html$', views.home, name='home'),
    # ex: /webD/readlist
    url(r'^readlist\.html$', views.readlist, name='readlist'),
    # ex: /webD/history/
    url(r'^history\.html$', views.history, name='history'),

    # ex: /webD/logout/
    url(r'^logout\.html$', views.logout, name='logout'),
]