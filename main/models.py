import datetime
from django.db import models
from django.utils import timezone

#------------------用户信息

# 表名
db_table_name_user = 'user'
db_table_name_user_login_log = 'user_login_log'
db_table_name_user_group = 'user_group'
db_table_name_member_ship = 'member_ship'
db_table_name_message = 'message'

'''
用户信息
'''
class User(models.Model):
    # 列名
    db_column_username = 'username'
    db_column_display_name = 'display_name'
    db_column_uid = 'uid'
    db_column_phone_number = 'phone_number'
    db_column_password = 'password'
    db_column_gender = 'gender'
    db_column_birthday = 'birthday'
    db_column_register_time = 'register_time'

    '''用户名'''
    username = models.CharField(max_length=32, db_column=db_column_username)
    '''用户名显示'''
    display_name = models.CharField(max_length=64, db_column=db_column_display_name)
    '''用户名ID'''
    uid = models.CharField(max_length=32, db_column=db_column_uid)
    '''电话号码'''
    phone_number = models.CharField(max_length=32, db_column=db_column_phone_number)
    '''用户密码'''
    password = models.CharField(max_length=128, db_column=db_column_password)
    '''性别'''
    GENDER = ((u'M', u'male'), # 男
           (u'F', u'female'), # 女
           (u'O', u'Other'), # 其他
           (u'S', u'Secret'),) # 保密
    gender = models.CharField(max_length=1, choices=GENDER, null=True, db_column=db_column_gender)

    '''用户生日'''
    birthday = models.DateTimeField(default=datetime.date.fromtimestamp(0), db_column=db_column_birthday)

    '''用户注册日期'''
    register_time = models.DateTimeField(auto_now_add=True, db_column=db_column_register_time)

    def __str__(self):
        return self.username

    class Meta:
        db_table = db_table_name_user

'''
用户登录记录
'''
class UserLoginLog(models.Model):
    # 表名
    db_table_name = 'user_login_log'
    # 列名
    db_column_ip= 'ip'
    db_column_time= 'time'

    owner = models.ForeignKey(User)
    ip = models.CharField(max_length=50, db_column=db_column_ip)
    time = models.DateTimeField(auto_now=True, db_column=db_column_time)

    def __str__(self):
        return '%s - %s' % (self.owner.name, self.time + self.ip)

    class Meta:
        db_table = db_table_name_user_login_log

'''
用户组信息
'''
class UserGroup(models.Model):
    # 表名
    db_table_name = 'user_group'
    # 列名
    db_column_name = 'name'

    name = models.CharField(max_length=128, db_column=db_column_name)
    user = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name

    class Meta:
        db_table = db_table_name_user_group

'''
用户与组关系
'''
class Membership(models.Model):
    # 表名
    db_table_name = 'member_ship'
    # 列名
    db_column_joined_date = 'joined_date'
    db_column_invite_reason = 'invite_reason'

    # 用户
    user = models.ForeignKey(User)
    # 组
    user_group = models.ForeignKey(UserGroup)
    # 加入日期
    joined_date = models.DateTimeField(db_column=db_column_joined_date)
    # 加入原因
    invite_reason = models.CharField(max_length=64, db_column=db_column_invite_reason)

    class Meta:
        db_table = db_table_name_member_ship


#------------------消息信息
'''
消息
'''
class Message(models.Model):
    # 表名
    db_table_name = 'message'
    # 列名
    db_column_title = 'title'
    db_column_content = 'content'
    db_column_last_modify_time = 'last_modify_time'
    db_column_create_time = 'create_time'
    db_column_owner = 'owner'

    # 消息标题
    title = models.CharField(max_length=64, db_column=db_column_title)
    # 消息内容
    content = models.CharField(max_length=1024, db_column=db_column_content)
    # 最后修改时间
    last_modify_time = models.DateTimeField(auto_now=True, db_column=db_column_last_modify_time)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, db_column=db_column_create_time)
    # 发布用户
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title

    class Meta:
        db_table = db_table_name_message

#------------------其他