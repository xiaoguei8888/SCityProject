from django.conf.urls import url

from publish import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'SCity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^$', views.index, name='index'),
]
