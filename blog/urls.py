from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)$', views.view, name='view'),
    url(r'^add-post$', views.add_post, name='add_post'),
]