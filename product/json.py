from django.core import serializers
from django.http import HttpResponse
from product.models import Product
from django.utils import timezone

import json

def test_all(request):
    print('product jsons all')
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def list(request):
    print('list all product with json format')
    latest_product_list = Product.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    data = serializers.serialize('json', latest_product_list)
    return HttpResponse(data, content_type='application/json')

def detail(request, id):
    print('product detail with id', id)
    product = Product.objects.get(id=id)
    data = serializers.serialize('json', product)
    return HttpResponse(data, content_type='application/json')
    pass