from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'SCity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^message/', include('message.urls', namespace='message')),
    url(r'^publish/', include('publish.urls', namespace='publish')),
]
