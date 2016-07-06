from django.conf.urls import url
from search import jsons

urlpatterns = [
    url(r'^$', jsons.parse, name='search'),
]
