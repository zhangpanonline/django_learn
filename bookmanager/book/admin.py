from django.contrib import admin
from book.models import BookInfo, PeopleInfo
# 注册模型类
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# 重新运行服务
