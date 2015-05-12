from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib import auth
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
                               required=True,
                               error_messages={'required': '请输入用户名',
                                               'min_length': '至少输入8个字符',
                                               'max_length': '至多输入32个字符', },
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '用户名',
                                                             'min_length': '8',
                                                             'max_length': '32',
                                                             }),)
    password = forms.CharField(label='',
                               min_length=8,
                               max_length=32,
                               required=True,
                               error_messages={'required': '请输入密码',
                                               'min_length': '至少输入8个字符',
                                               'max_length': '至多输入32个字符', },
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'type': 'password',
                                                             'placeholder': '密码',
                                                             'min_length': '8',
                                                             'max_length': '32',
                                                             }),)

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
        if login_form.is_valid():
            error_messages = None

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            else:
                error_messages = '请开启浏览器的Cookie'
            #获取表单用户密码
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            if not username:
                error_messages = '请输入用户名'
            elif not password:
                error_messages = '请输入密码'

            if username is not None and password is not None:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        # 转到主页面
                        return login_success(username)
                    else:
                        error_messages = '当前账户不可用'
                else:
                    error_messages = '用户无效'

            context = RequestContext(request, {'login_form':login_form,
                                           'error_messages':error_messages,})
            return render(request, './main/login.html', context)
    request.session.set_test_cookie()
    login_form = LoginForm()
    context = RequestContext(request, {'login_form':login_form})
    return render(request, './main/login.html', context)

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
    username = forms.CharField(label='',
                               required=True,
                               error_messages={'required': '请输入用户名',
                                               'min_length': '至少输入8个字符',
                                               'max_length': '至多输入32个字符', },
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '请输入用户名',
                                                             'min_length': '8',
                                                             'max_length': '32',
                                                             }),)
    password = forms.CharField(label='',
                               min_length=8,
                               max_length=32,
                               required=True,
                               error_messages={'required': '请输入密码',
                                               'min_length': '至少输入8个字符',
                                               'max_length': '至多输入32个字符', },
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'type': 'password',
                                                             'placeholder': '请输入密码',
                                                             'min_length': '8',
                                                             'max_length': '32',
                                                             }),)
    password_again = forms.CharField(label='',
                               min_length=8,
                               max_length=32,
                               required=True,
                               error_messages={'required': '请再次输入密码',
                                               'min_length': '至少输入8个字符',
                                               'max_length': '至多输入32个字符', },
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'type': 'password',
                                                             'placeholder': '请确认密码',
                                                             'min_length': '8',
                                                             'max_length': '32',
                                                             }),)
    phone_number = forms.CharField(label='',
                               min_length=8,
                               max_length=32,
                               required=True,
                               error_messages={'required': '请输入手机号码',
                                               'min_length': '至少输入8个字符',
                                               'max_length': '至多输入32个字符', },
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '请输入手机号码',
                                                             'min_length': '8',
                                                             'max_length': '32',
                                                             }),)

def register(request):
    print('register')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid() :
            #获取表单用户信息
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            password_again = register_form.cleaned_data['password_again']
            phone_number = register_form.cleaned_data['phone_number']
            #获取的表单数据与数据库进行比较
            error_messages = ''
            if password != password_again:
                error_messages = '两次输入密码不相同'
            elif User.objects.filter(username__exact = username):
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


#--------------------------------------------
def meta(request):
    user_meta = request.META.items()
    print(user_meta)
    context = RequestContext(request, {'user_meta':user_meta,})
    return render(request, './main/meta.html', context)

