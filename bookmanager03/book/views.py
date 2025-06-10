from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    print("查询字符串为：",request.GET)
    print("请求方法为：",request.method)


    return HttpResponse("index")

from django.http import JsonResponse
def goods(request,shop_id,goods_id):

    return JsonResponse({'shop_id':shop_id,'goods_id':goods_id})

def get_header(request):
    #获取请求头信息
    print(request.META.get('SERVER_PORT'))
    print(request.META.get('SERVER_NAME'))

    return HttpResponse('header')

def get_http_method(request):
    # 获取http请求方法
    method=request.method
    print(method)
    return HttpResponse(method)

def response(request):
    response = HttpResponse('incast python')
    response.status_code=400
    response['itcast'] = 'Python' #自定义响应头，值为Python
    return response

import json
def returnjson(request):

    data = [
        {
            'name':'cheney'
            'gender'"male"
        },
        {
            'name':'honey'
            'gender'"female"
        },

    ]

    # data = json.dumps(data)
    return JsonResponse(data,safe=False)



#重定向
from django.shortcuts import redirect
def redirect_url(request):
    url = 'http://www.bing.com'

    return redirect(url)



def set_cookie(request):
    """"
    def set_cookie(
        self,
        key,
        value="",
    """
    response = HttpResponse('ok')
    response.set_cookie('username','cheney')
    return response


def get_cookie(request):
    cookie1 = request.COOKIES.get('username')
    print(cookie1)
    return HttpResponse(f'get_cookie:{cookie1}')

def del_cookie(request):
    cookie1 = request.COOKIES.get('username')
    response = HttpResponse(f'get_cookie:{cookie1}')
    response.delete_cookie('username')
    print(cookie1)
    return response