from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import Bookinfo
def index(request):

    #在这里实现 增删改查
    [book.id for book in Bookinfo.objects.all()]
    [book.id for book in Bookinfo.objects.all()]
    [book.id for book in Bookinfo.objects.all()]
    [book.id for book in Bookinfo.objects.all()]
    [book.id for book in Bookinfo.objects.all()]



    books = Bookinfo.objects.all()
    [book.id for book in books]
    [book.id for book in books]
    [book.id for book in books]
    [book.id for book in books]
    [book.id for book in books]
    [book.id for book in books]

    print(books)


    return HttpResponse("index")

# name = 'abc'
# mysql 的数据存储在 硬盘
# redis 的数据存储在 内存

# 把硬盘的数据存储在内存 也称之为 缓存

##############增加数据########################
from book.models import Bookinfo
# 方式1
book=Bookinfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 必须要调用 对象的save()方法才能将数据保存大奥数据库中
book.save()

# 方式2
#objects -- 相当于一个代理，实现增删改查
#

Bookinfo.objects.create(
    name='测试开发',
    pub_date='2020-1-1',
    readcount=100
)


###################修改数据################################

# 方式1
# select * from Bookinfo where id=6
book=Bookinfo.objects.get(id=6)

book.name='运维开发入门'

#想要保存数据 需要调用 对象的save方法
book.save()

# 方式2
# filter 过滤
Bookinfo.objects.filter(id=6).update(name='爬虫',commentcount=666)

# 错误的
# Bookinfo.objects.get(id=5).update(name='555',commentcount=999)

###############删除数据######################
# 方式1

book=Bookinfo.objects.get(id=6)

#删除分两种 物理删除(这条记录的数据 删除) 和 逻辑删除(修改标记 例如 is_delete=False)

book.delete()

# 方式2
Bookinfo.objects.get(id=6).delete()
Bookinfo.objects.filter(id=5).delete()

################查询####################

# get查询单一结果，如果不存在会抛出类模型.DoesNotExist异常。
try:
    book=Bookinfo.objects.get(id=1)
except Bookinfo.DoesNotExist:
    print('查询结果不存在')
# all查询多个结果
Bookinfo.objects.all()
from book.models import Peopleinfo
Peopleinfo.objects.all()

# count查询结果数量
Bookinfo.objects.all().count()
Bookinfo.objects.count()

#######################过滤查询########################
# 实现SQL中的where功能，包括
# filter过滤出多个结果
# exclude排除掉符合条件的结果
# get过滤单一结果

# 模型类名.objects.filter(属性名__运算符==值)   获取n个结果 n=0,1,2,...
# 模型类名.objects.exclude(属性名__运算符==值)  获取n个结果 n=0,1,2,...
# 模型类名.objects.get(属性名__运算符==值)      获取1个结果 或者 异常

# 查询编号为1的图书
book=Bookinfo.objects.get(id=1)        #简写形式(属性名=值)
book=Bookinfo.objects.get(id__exact=1) #完整形式(id__exact=1)

Bookinfo.objects.get(pk=1) # pk primary key 主键

Bookinfo.objects.get(id=1)
Bookinfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
Bookinfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
Bookinfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
Bookinfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
Bookinfo.objects.filter(id__in=[1,3,5])
Bookinfo.objects.filter(id__in=(1,3,5,))

# 查询编号大于3的图书
# 大于 gt        greater than 大于
# 大于等于 gte    e equal
# 小于 ls        less than
# 小于等于 lte
Bookinfo.objects.filter(id__gt=3)

# 查询编号不等于3的书籍
Bookinfo.objects.exclude(id=3)

# 查询1980年发表的图书
Bookinfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
Bookinfo.objects.filter(pub_date__gt='1990-1-1')
Bookinfo.objects.filter(pub_date__gt='19900101')

# 错误的 Bookinfo.objects.filter(pub_date__gt='1990011')

##############################################################

from django.db.models import F

# 使用：2个属性的比较
# 语法形式： 以filter为例  模型类名.objects.filter(属性名__运算符=F('第二个属性名')）

#查询阅读量大于等于评论量的图书
Bookinfo.objects.filter(readcount__gt=F('commentcount'))

#############################################################

# 并且查询
# 查询阅读量大于20，并且编号小于3的图书。

Bookinfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者
Bookinfo.objects.filter(readcount__gt=20,id__lt=3)

# 或者查询
# 查询阅读量大于20，或者编号小于3的图书。

from django.db.models import Q

#或者语法： 模型类名.onjects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
#并且语法： 模型类名.onjects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
#not 非语法： 模型类名.onjects.filter(~Q(属性名__运算符=值))

Bookinfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# 查询编号不等于3的书籍
Bookinfo.objects.exclude(id__exact=3)
Bookinfo.objects.filter(~Q(id__exact=3))

########################聚合函数#####################################

from django.db.models import Sum,Min,Max,Avg,Count

# 模型类名.objects.aggregate(Xxx('字段名'))

Bookinfo.objects.aggregate(Sum('readcount'))

#######################排序######################################
Bookinfo.objects.all().order_by('readcount') #升序
Bookinfo.objects.all().order_by('-readcount') #降序


########################级联操作##############################

#查询书籍为1的所有人物信息

#获取了id为1的书籍
book=Bookinfo.objects.get(id=1)
book.peopleinfo_set.all()

# Peopleinfo.objects.filter(book=1)

#查询人物为1书籍信息
person=Peopleinfo.objects.get(id=1)

person.book.name
person.book.readcount

################关联过滤查询########################

# 语法形式
# 查询1的数据，条件为 n
# 模型类名.objects.(模型类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为"郭靖"
Bookinfo.objects.filter(peopleinfo__name__exact='郭靖')
Bookinfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
Bookinfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
Peopleinfo.objects.filter(book__name__exact='天龙八部')
Peopleinfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30的所有人物
Peopleinfo.objects.filter(book__readcount__gt=30)


