from django.conf.urls import url

from product import views
from product import jsons

urlpatterns = [
    # Examples:
    # url(r'^$', 'SCity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^$', jsons.all, name='all'),
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)/', views.detail, name='detail'),
    # url(r'^product', views.product, name='product'),
]
