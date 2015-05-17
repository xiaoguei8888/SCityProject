from django.contrib import admin

from publish.models import Publish

#------------------消息

class PublishAdmin(admin.ModelAdmin):
    list_display = (Publish.db_column_title,
                    Publish.db_column_content,
                    Publish.db_column_last_modify_time,
                    Publish.db_column_create_time,)
    fieldsets = [
        ('Message', {'fields':[Publish.db_column_title, Publish.db_column_content, Publish.db_column_owner]}),
    ]

    list_filter = [Publish.db_column_create_time,]
    search_fields = [Publish.db_column_title, Publish.db_column_content,]
    # 最后修改的时间排序
    ordering = (Publish.db_column_last_modify_time,)

admin.site.register(Publish, PublishAdmin)

#------------------其他