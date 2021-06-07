from moments.models import Status, WeChatUser
from django.contrib import admin
from .models import WeChatUser, Status
# Register your models here.

# 启用admin APP
admin.site.register(WeChatUser)
admin.site.register(Status)