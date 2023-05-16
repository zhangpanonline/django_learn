from django.db import models

# Create your models here.


"""
1. 我们的模型类需要继承自 models.Model
2. 系统会自动添加一个主键 id
3. 字段定义
    字段名=models.类型(选项)
    
    字段名不要使用 python、mysql 等关键字
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    # 重写 __str__ 方法，来在后台管理系统显示书籍名字
    def __str__(self):
        return self.name


# 人物
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


