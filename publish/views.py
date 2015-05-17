from django.shortcuts import render

from django.utils import timezone
# Create your views here.
from django.template import RequestContext
from publish.models import Publish

'''
消息列表页面
'''
def index(request):
    print('publish index')
    username = request.COOKIES.get('username')
    latest_publish_list = Publish.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    context = RequestContext(request, {'username':username,
                                       'latest_publish_list':latest_publish_list,}
                             );
    return render(request, './publish/index.html', context)