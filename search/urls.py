from django.conf.urls import url
from search import json

urlpatterns = [
    url(r'^$', json.parse, name='search'),
]
