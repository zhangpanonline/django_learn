"""
1. 我们的模型类需要继承自 models.Model
2. 系统会自动添加一个主键 id
3. 字段定义
    3.1 属性
        字段名=models.类型(选项)
        字段名不要使用 python、mysql 等关键字
        字段名不要使用连续的下划线（__），因为后面的查询会用到 __
    3.2 类型   MySQL的类型
    3.3 选项  是否有默认值、是否唯一、是否为 null
             CharField 必须设置 max_length
             verbose_name 主要是 admin 站点使用
4. 改变表的名称
    默认表的名称是：子应用名_类名 都是小写
    修改表的名字 使用 class Meta: db_table = ''
"""
from django.db import models


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='名称')
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # 系统会自动添加一个 peopleinfo_set=[PeopleInfo, PeopleInfo, ...] 的隐藏字段
    class Meta:
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '书籍管理'  # 在 admin 站点中显示的名称

    def __str__(self):
        return self.name  # 定义每个数据对象的显示信息


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1, verbose_name='性别')
    description = models.CharField(verbose_name='描述', max_length=100, null=True)
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    # 外键
    # 系统会自动为外键添加 _id

    # 外键的级联操作
    # 主表 和 从表
    #  1  对 多
    # 书籍 对 人物

    # 主表的一条数据 如果删除了
    # 从表有关联的数据，关联的数据怎么办呢？
    # SET_NULL 抛出异常，不让删除
    # CASCADE 级联删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name







