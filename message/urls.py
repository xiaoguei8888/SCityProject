from django.conf.urls import url

from message import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'SCity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/', views.detail, name='detail'),
    url(r'^publish$', views.publish, name='publish'),
]
