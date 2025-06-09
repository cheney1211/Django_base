from django.http import HttpResponse
from django.shortcuts import render, redirect
from book.models import BookInfo
# Create your views here.
def create_book(request):

    book = BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )

    return HttpResponse("create")

def shop(request,city_id,mobile):

    # import re
    # if not re.match('\d{5}',shop_id):
    #     return HttpResponse("没有此商品")
    print(city_id,mobile)

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

def register(request):
    data=request.POST
    print(data)
    # < QueryDict: {'username': ['cheney'], 'password': ['0514']} >
    return HttpResponse("ok")

def json(request):

    #request.POST   json数据不能通过request.POST获取数据
    body=request.body
    # print(body)
    body_str=body.decode()
    # print(body_str)
    """
    {
        "name":"cheney",
        "age":10
    }
    """
    # print(type(body_str))

    # JSON形式的字符串 可以穿换位Python的字典
    import json
    body_dict=json.loads(body_str)
    # print(body_dict)

    ###############请求头#################
    # print(request.META)
    # print(request.META.get('SERVER_PORT'))
    print(request.META['SERVER_PORT'])

    return HttpResponse("json")

def method(request):
    print(request.method)
    return HttpResponse("method")

from django.http import HttpResponse,JsonResponse
def response(resquest):
    # JSON-->dict
    # dict-->JSON
    info ={
        'name':'cheney',
        'address':'chongqing'
    }
    girl_friends=[
        {
            'name': 'rose',
            'address': 'chongqing'
        },
        {
            'name': 'yifei',
            'address': 'wuhan'
        }
    ]


    # data 返回的响应数据 一般是字典类型
    """
    safe = True 是表示 我们的data 是字典数据
    JsonResponse 可以把字典转换为JSON
    
    现在给了一个非字典数据，除了问题 我们自己负责
    """

    # response=JsonResponse(data=girl_friends,safe=False)
    # # response=JsonResponse(data={'name':'cheney'})
    # return response

    # import json
    # data = json.dumps(girl_friends)
    # response=HttpResponse(data)
    # return response

    #重定向
    return redirect('http://www.baidu.com')

    # return HttpResponse('res',status=200)

    # 响应头的设置
    # response = HttpResponse('res',status=200)
    # response['name']='cheney'
    # return response

    # 1XX
    # 2XX
    #   200 成功
    # 3XX
    # 4XX  请求有问题
    #   404 找不到页面 路由有问题
    #   403 禁止访问   权限问题
    # 5XX
    # HTTP status code must be an integer from 100 to 599.
#####################################3
"""
查询字符串
https://ip.port/path/path/?kry=value&key1=value1

url 以 ? 为分别 分为2部分
?前边为 请求路径
?后边为 查询字符串 类似于字典 key=value 多个数据采用&拼接
"""