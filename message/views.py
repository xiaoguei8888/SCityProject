from django.shortcuts import render
from django.template import RequestContext
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django import forms

from message.models import Message
from main.models import User

'''
消息列表页面
'''
def index(request):
    print('message index')
    username = request.COOKIES.get('username')
    latest_message_list = Message.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    context = RequestContext(request, {'username':username,
                                       'latest_message_list':latest_message_list,}
                             );
    return render(request, './message/index.html', context)

'''
消息详情页面
'''
def detail(request, id):
    print('message detail', id)
    username = request.COOKIES.get('username')
    message = Message.objects.get(id=id)
    context = RequestContext(request, {'username':username,
                                       'message':message,}
                             );
    return render(request, './message/detail.html', context)

'''
定义消息表单模型
'''
class PublishMessageForm(forms.Form):
    title = forms.CharField(label='',
                               max_length=64,
                               min_length=8,
                               error_messages={'required':'请输入消息标题',
                                               'max_length':'最多输入64个字符',
                                               'min_length':'至少输入8个字符',},
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder':'请输入消息标题',}),)
    content = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder':'请输入消息内容',
                                                             }),
                               max_length=1024,
                               min_length=8,
                               error_messages={'required':'请输入消息内容',
                                               'max_length':'最多输入1024个字符',
                                               'min_length':'至少输入8个字符',},)

def publish(request):
    print('message publish')
    if request.method == 'POST':
        publish_message_form = PublishMessageForm(request.POST)
        if publish_message_form.is_valid():
            #获取表单信息标题和内容
            title = publish_message_form.cleaned_data['title']
            content = publish_message_form.cleaned_data['content']
            #获取的表单数据与数据库进行比较
            error_messages = ''
            title_len = str.__len__(title)
            if title_len == 0:
                error_messages = '没有标题内容'
            elif title_len > Message.db_column_title_max_length:
                error_messages = '标题太长'
            content_len = str.__len__(content)
            if content_len == 0:
                error_messages = '没有内容'
            elif content_len > Message.db_column_content_max_length:
                error_messages = '内容太长'

            if error_messages == '':
                Message.objects.create(title = title,
                                    content = content,
                                    owner = User.objects.get(id=1),
                                    )
                return HttpResponseRedirect(reverse("message:index"))
            else:
                context = RequestContext(request, {'publish_message_form':publish_message_form,
                                           'error_messages':error_messages,})
                return render(request, './message/publish.html', context)
    else:
        publish_message_form = PublishMessageForm()

    return render(request, './message/publish.html', {'publish_message_form': publish_message_form})