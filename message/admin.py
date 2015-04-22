from django.contrib import admin

from message.models import Message

#------------------消息

class MessageAdmin(admin.ModelAdmin):
    list_display = (Message.db_column_title,
                    Message.db_column_content,
                    Message.db_column_last_modify_time,
                    Message.db_column_create_time,)
    fieldsets = [
        ('Message', {'fields':[Message.db_column_title, Message.db_column_content, Message.db_column_owner]}),
    ]

    list_filter = [Message.db_column_create_time,]
    search_fields = [Message.db_column_title, Message.db_column_content,]
    # 最后修改的时间排序
    ordering = (Message.db_column_last_modify_time,)

admin.site.register(Message, MessageAdmin)

#------------------其他