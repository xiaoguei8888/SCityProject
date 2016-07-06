from django.core import serializers
from django.http import HttpResponse
from product.models import Product
from django.utils import timezone

KEYWORD = 'keyword'

'''
解析搜索请求
'''
def parse(request):
    if request.method == 'GET':
        queryDict = request.GET
    elif request.method == 'POST':
        queryDict = request.POST

    if queryDict.__contains__(KEYWORD):
        search_keyword = queryDict.__getitem__(KEYWORD)
        print(KEYWORD, search_keyword)

    latest_product_list = Product.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    data = serializers.serialize('json', latest_product_list)
    return HttpResponse(data, content_type='application/json')