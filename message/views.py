from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone

from message.models import Message

def index(request):
    print('message index')
    username = request.COOKIES.get('username')
    latest_message_list = Message.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    context = RequestContext(request, {'username':username,
                                       'latest_message_list':latest_message_list,}
                             );
    return render(request, './message/index.html', context)

def detail(request, id):
    print('message detail', id)
    username = request.COOKIES.get('username')
    message = Message.objects.get(id=id)
    context = RequestContext(request, {'username':username,
                                       'message':message,}
                             );
    return render(request, './message/detail.html', context)
