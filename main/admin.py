from django.contrib import admin

from main.models import User, UserLoginLog, UserGroup, Message

#------------------用户

class MessageInLine(admin.TabularInline):
    model = Message

class UserLoginLogInLine(admin.TabularInline):
    model = UserLoginLog

class UserAdmin(admin.ModelAdmin):
    list_display = (User.db_column_uid,
                    User.db_column_username,
                    User.db_column_display_name,
                    User.db_column_gender,
                    User.db_column_phone_number,
                    User.db_column_register_time,)
    fieldsets = [
        ('Uid', {'fields':[User.db_column_uid]}),
        ('Username', {'fields':[User.db_column_username]}),
        ('Display Name', {'fields':[User.db_column_display_name]}),
        ('Gender', {'fields':[User.db_column_gender]}),
        ('Phone Number', {'fields':[User.db_column_phone_number]}),
    ]

    inlines = [MessageInLine, UserLoginLogInLine]

    list_filter = [User.db_column_register_time, User.db_column_gender,]
    search_fields = [User.db_column_username, User.db_column_display_name,]
    ordering = (User.db_column_register_time,)

admin.site.register(User, UserAdmin)
admin.site.register(UserGroup)


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