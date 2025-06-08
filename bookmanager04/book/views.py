from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.
def create_book(request):

    book = BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )

    return HttpResponse("create")

def shop(request,city_id,shop_id):

    query_params=request.GET
    print(query_params)
    # order = query_params.get('order')
    # order = query_params['order']
    # print(order)

    # < QueryDict: {'order': ['readcount']} >
    # QueryDict 具有字典的特性
    # 还具有 一键多值
    # < QueryDict: {'order': ['readcount', 'commentcount'], 'page': ['1']} >
    order = query_params.getlist('order')

    print(order)

    return HttpResponse("杨哥的小饭店")


#####################################3
"""
查询字符串
https://ip.port/path/path/?kry=value&key1=value1

url 以 ? 为分别 分为2部分
?前边为 请求路径
?后边为 查询字符串 类似于字典 key=value 多个数据采用&拼接
"""