from django.contrib import admin

from product.models import Product

#------------------产品

class ProductAdmin(admin.ModelAdmin):
    list_display = (Product.db_column_name,
                    Product.db_column_desc,
                    Product.db_column_price,
                    Product.db_column_image,
                    Product.db_column_last_modify_time,
                    Product.db_column_create_time,)
    fieldsets = [
        ('Product', {'fields':[Product.db_column_name, Product.db_column_desc, Product.db_column_price,
                               Product.db_column_image]}),
    ]

    list_filter = [Product.db_column_create_time,]
    search_fields = [Product.db_column_name, Product.db_column_desc,]
    # 最后修改的时间排序
    ordering = (Product.db_column_last_modify_time,)

admin.site.register(Product, ProductAdmin)

#------------------其他