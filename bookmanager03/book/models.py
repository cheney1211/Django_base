from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    name=models.CharField(max_length=10,verbose_name='书名')
    pub_date = models.DateField(verbose_name='发布时间')
    readcount = models.IntegerField(default=0,verbose_name='阅读量')
    commentcount = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        """定义每个数据对象显示的名称"""
        return self.name

    class Meta:
        db_table = 'bookinfo' #指明数据库表名
        verbose_name = '图书'  #在admin站点显示的名称


class Peopleinfo(models.Model):

    GENDER_CHOICE=(
        (1,'male'),
        (2,'female'),
    )

    name=models.CharField(max_length=10,verbose_name='人名')
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,verbose_name='性别')
    description=models.CharField(max_length=10,verbose_name='描述信息',null=True)
    is_delete=models.BooleanField(default=False,verbose_name='是否删除')
    book_id=models.ForeignKey(Bookinfo,on_delete=models.CASCADE,verbose_name='图书') # 外键

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        """定义每个对象的显示信息"""
        return self.name

