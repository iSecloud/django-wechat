from moments.models import Status, WeChatUser, Reply
from django.contrib import admin
from .models import Reply, WeChatUser, Status
# Register your models here.

# 启用admin APP

class StatusAdmin(admin.ModelAdmin): #添加功能
    list_display = ["text", "user", "pub_time"] #展示信息
    search_fields = ["text", "user__user__username"] #status的user外键到Wechat_user在一对一到django中的user的username
    date_hierarchy = "pub_time"
    list_filter = ["pub_time"] #过滤器

admin.site.register(WeChatUser)
admin.site.register(Status, StatusAdmin)
admin.site.register(Reply)