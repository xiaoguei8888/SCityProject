from django.db import models

from django.contrib.auth.models import User


#------------------产品信息

db_table_name_message = 'product'

'''
产品
'''
class Product(models.Model):
    # 表名
    db_table_name = 'product'
    # 列名
    db_column_name = 'name'
    db_column_desc = 'desc'
    db_column_price = 'price'
    db_column_image = 'image'
    db_column_last_modify_time = 'last_modify_time'
    db_column_create_time = 'create_time'

    db_column_name_max_length = 64
    db_column_desc_max_length = 1024
    db_column_image_max_length = 512

    # 产品名
    name = models.CharField(max_length=db_column_name_max_length, db_column=db_column_name, verbose_name='产品名')
    # 产品描述
    desc = models.CharField(max_length=db_column_desc_max_length, db_column=db_column_desc, verbose_name='产品描述')
    # 产品价格
    price = models.BigIntegerField(db_column=db_column_price, verbose_name='产品价格')
    # 产品图片
    image = models.CharField(max_length=db_column_image_max_length, db_column=db_column_image, verbose_name='产品图片')
    # 最后修改时间
    last_modify_time = models.DateTimeField(auto_now=True, db_column=db_column_last_modify_time)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, db_column=db_column_create_time)

    def __str__(self):
        return self.name

    class Meta:
        db_table = db_table_name_message