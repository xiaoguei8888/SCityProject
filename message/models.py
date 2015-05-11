from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


#------------------消息信息

db_table_name_message = 'message'

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

    db_column_title_max_length = 64
    db_column_content_max_length = 1024

    # 消息标题
    title = models.CharField(max_length=db_column_title_max_length, db_column=db_column_title, verbose_name='消息标题')
    # 消息内容
    content = models.CharField(max_length=db_column_content_max_length, db_column=db_column_content)
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