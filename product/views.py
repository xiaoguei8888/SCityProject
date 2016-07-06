from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import forms

from product.models import Product
from django.contrib.auth.models import User

'''
产品列表页面
'''
def list(request):
    print('product list')
    username = request.COOKIES.get('username')
    latest_product_list = Product.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    context = RequestContext(request, {'username':username,
                                       'latest_product_list':latest_product_list,}
                             );
    return render(request, './product/list.html', context)

'''
产品详情页面
'''
def detail(request, id):
    print('product detail', id)
    username = request.COOKIES.get('username')
    message = Product.objects.get(id=id)
    context = RequestContext(request, {'username':username,
                                       'product':message,}
                             );
    return render(request, './product/detail.html', context)