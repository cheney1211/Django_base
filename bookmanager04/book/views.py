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


################Cookie和Session#########################
"""
第一次请求，携带 查询字符串
http://localhost:8000/set_cookie/?username=cheney&password=0514
服务器接收到请求之后，获取username，服务器设置Cookie信息，Cookie信息包括 username
浏览器接收到服务器的响应之后，应该把Cookie保存起来

第二次及其之后的请求，我们访问http://localhost:8000 都会携带Cookie信息。服务器就可以读取Cookie信息，来判断用户身份
"""

def set_cookie(request):
    # 1.获取查询字符串的数据
    username=request.GET.get('username')
    password=request.GET.get('password')
    # 2.服务器设置Cookie信息
    # 通过响应对象.set_cookie 方法
    response = HttpResponse("set_cookie")
    # key,
    # value = "",
    # max_age 是一个秒数 从响应开始 计数的一个秒数
    response.set_cookie('name',username,max_age=60*60)
    response.set_cookie('pwd',password)
    return response

def get_cookie(request):
    # 获取Cookie

    print(request.COOKIES)
    # request.COOKIES 字典数据
    name = request.COOKIES.get('name')
    # password = request.COOKIES.get('pwd')
    return HttpResponse(content=name)


############################################################################

# session 是保存在服务器端 -- 数据相对安全
# session需要依赖于Cookie

"""
第一次请求 http://127.0.0.1:8000/set_session/?username=cheney ，我们在服务器端设置session信息
服务器同时会生成sessionid的Cookie信息。
浏览器接收到这个信息之后，会把Cookie数据保存起来

第二次及其之后的请求 都会携带这个sessionid，服务器会验证这个sessionid，验证没有问题会读取相关数据，实现业务逻辑

"""

def set_session(request):

    # 1.模拟 获取用户信息
    username=request.GET.get('username')
    # 2.设置session信息
    # 假如 我们通过模型查询 查询到了 用户的信息
    user_id=1

    request.session['user_id']=user_id
    request.session['username']=username


    # clear 删除session里的数据，但是 key有保留
    # request.session.clear()
    # flush 删除session里的数据.包括key
    # request.session.flush()

    # 设置session的有效期
    request.session.set_expiry(3600)


    return HttpResponse("set_session")

def get_session(request):

    # user_id = request.session['user_id']
    # username = request.session['username']

    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = "{},{}".format(user_id, username)

    return HttpResponse(content)


##########################类视图##################################

def login(request):

    print(request.method)
    # 使用method属性获取请求类别
    if request.method == "GET":
        return HttpResponse("get 逻辑")
    else:
        return HttpResponse("post 逻辑")


"""
类视图的定义
class 类视图名字(View):
    def get(self,request):
        
        return HttpResponse('xxx')
        
    def http_method_lower(self,request):
        
        return HttpResponse('xxx')
        
1.继承自View
2.类视图中的方法 是采用 http方法小写来区分不同的请求方式
"""

from django.views import View
class LoginView(View):

    def get(self,request):
        return HttpResponse('get get get')

    def post(self,request):

        return HttpResponse('post post post')


#复习
# class Person(object):
#
#     # 对象方法
#     def play(self):
#         pass
#     # 类方法
#     @classmethod
#     def say(cls):
#         pass
#     # 静态方法
#     @staticmethod
#     def eat():
#         pass
#
# Person.say()