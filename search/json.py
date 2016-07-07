from django.core import serializers
from django.http import HttpResponse
from product.models import Product
from django.utils import timezone

import json

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
        # 包含关键字
        search_keyword = queryDict.__getitem__(KEYWORD)
        print(KEYWORD, search_keyword)
        # TODO 需要对于请求关键字做判断，防止被不良使用
        if len(search_keyword.strip()) > 0:
            response = search(search_keyword)
        else:
            response = search_keyword_invalid(search_keyword)
    else:
        # 不包含关键字
        response = search_request_forbidden()
    return response


RESULT_CODE_SUCCESS = 0
RESULT_CODE_FORBIDDEN = -1
RESULT_CODE_INVALID_KEYWORD = -2

RESULT_TYPE_SUCCESS = 'SUCCESS'
RESULT_TYPE_ERROR = 'ERROR'

RESULT_INFO_SUCCESS = 'success'
RESULT_INFO_FORBIDDEN = 'request is forbidden'
RESULT_INFO_INVALID_KEYWORD = 'invalid keyword'

'''
根据关键字搜索
'''


def search(keyword):
    print('search by keyword', keyword)
    results = Product.objects.filter(name__contains=keyword)
    print('results', results)
    data = serializers.serialize('json', results)
    json_data = create_json_response(keyword,
                                     RESULT_CODE_SUCCESS,
                                     RESULT_TYPE_SUCCESS,
                                     RESULT_INFO_SUCCESS,
                                     data)
    return HttpResponse(json_data, content_type='application/json')


'''
搜索请求被禁止
'''


def search_request_forbidden():
    data = {}
    json_data = create_json_response(None,
                                     RESULT_CODE_FORBIDDEN,
                                     RESULT_TYPE_ERROR,
                                     RESULT_INFO_FORBIDDEN,
                                     data)
    return HttpResponse(json_data, content_type='application/json')


'''
搜索关键字出错
'''


def search_keyword_invalid(keyword):
    data = {}
    json_data = create_json_response(keyword,
                                     RESULT_CODE_INVALID_KEYWORD,
                                     RESULT_TYPE_ERROR,
                                     RESULT_INFO_INVALID_KEYWORD,
                                     data)
    return HttpResponse(json_data, content_type='application/json')


'''
构建json响应
'''


def create_json_response(keyword, response_code, response_type, response_info, json_data):
    result_data = {}
    response_data = {}
    result_data['info'] = response_code
    result_data['type'] = response_type
    result_data['code'] = response_info
    if not keyword:
        response_data['keyword'] = keyword
    response_data['response'] = result_data
    response_data['data'] = json_data
    json_response = json.dumps(response_data)
    return json_response
