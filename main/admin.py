from django.contrib import admin

from main.models import User, UserLoginLog, UserGroup
from message.models import Message

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

#------------------其他