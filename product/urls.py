from django.conf.urls import url

from product import views
from product import json

urlpatterns = [
    # json
    url(r'^$', json.list, name='list'),
    url(r'^(\d+)/', json.detail, name='detail'),
    # views
    # url(r'^$', views.list, name='list'),
    # url(r'^(\d+)/', views.detail, name='detail'),
]
