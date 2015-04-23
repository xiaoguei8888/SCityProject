from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from main.models import User
from message.models import Message
from django import forms

#--------------------------------------------

def index(request):
    print('index')
    username = request.COOKIES.get('username')
    latest_message_list = Message.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')[:5]
    context = RequestContext(request, {'username':username,
                                       'latest_message_list':latest_message_list,}
                             );
    return render(request, './main/index.html', context)

'''
定义登录表单模型
'''
class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               max_length=32,
                               error_messages={'required':'请输入用户名',},
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder':'Username',}),)
    password = forms.CharField(label='',
                               help_text="为了您的帐户安全，请至少输入8个字符，最多可输入128个字符",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'type':'password',
                                                             'placeholder':'Password',
                                                             }),
                               max_length=128,
                               min_length=8,
                               error_messages={'required':'请输入密码',
                                               'max_length':'最多输入128个字符',
                                               'min_length':'至少输入8个字符',},)

'''
登录成功，跳转到主界面
'''
def login_success(username = None):
    # 跳转到主页面
    response = HttpResponseRedirect(reverse("main:index"))
    # 设置cookie
    response.set_cookie('username', username, 3600)
    return response

def login(request):
    print('login')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid() :
            #获取表单用户密码
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            error_messages = ''
            if not User.objects.filter(username__exact = username):
                error_messages = '用户名不存在'
            elif not User.objects.filter(password__exact = password):
                error_messages = '密码错误'

            if error_messages == '':
                # 调转到主页面
                return login_success(username=username)
            else:
                context = RequestContext(request, {'login_form':login_form,
                                           'error_messages':error_messages,});
                return render(request, './main/login.html', context)
    else:
        login_form = LoginForm()

    return render(request, './main/login.html', {'login_form': login_form})

'''
登出
'''
def logout(request):
    print('logout')
    # 调转到主页面
    response = HttpResponseRedirect(reverse("main:index"))
    # 删除cookie
    response.delete_cookie('username')
    return response


'''
定义注册表单模型
'''
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    phone_number = forms.CharField(label='手机号码', max_length=20)

def register(request):
    print('register')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid() :
            #获取表单用户信息
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            phone_number = register_form.cleaned_data['phone_number']
            #获取的表单数据与数据库进行比较
            error_messages = ''
            if User.objects.filter(username__exact = username):
                error_messages = '用户名已注册'
            elif User.objects.filter(phone_number__exact = phone_number):
                error_messages = '手机号码已注册'

            if error_messages == '':
                User.objects.create(username = username,
                                    password = password,
                                    phone_number = phone_number,)
                # 调转到主页面
                return login_success(username=username)
            else:
                context = RequestContext(request, {'register_form':register_form,
                                           'error_messages':error_messages,}
                                         );
                return render(request, './main/register.html', context)
    else:
        register_form = RegisterForm()

    return render(request, './main/register.html', {'register_form': register_form})