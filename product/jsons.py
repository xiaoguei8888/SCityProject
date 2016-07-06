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

def all(request):
    print('product jsons all')
    latest_product_list = Product.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    data = serializers.serialize('json', latest_product_list)
    return HttpResponse(data, content_type='application/json')