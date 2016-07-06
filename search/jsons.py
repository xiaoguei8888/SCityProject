from django.core import serializers
from django.http import HttpResponse
from product.models import Product
from django.utils import timezone


def do_something():
    pass

def do_something_else():
    pass

'''
解析搜索请求
'''
def parse(request):
    print('product jsons all', request)
    if request.method == 'GET':
        queryDict = request.GET
        do_something()
    elif request.method == 'POST':
        queryDict = request.POST
        do_something_else()
    if queryDict.__contains__('name'):
        search_name = queryDict.__getitem__('name')
    print('search', search_name)

    latest_product_list = Product.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    data = serializers.serialize('json', latest_product_list)
    return HttpResponse(data, content_type='application/json')