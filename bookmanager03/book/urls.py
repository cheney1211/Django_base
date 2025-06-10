from django.urls import path
from book.views import (index,goods,get_header,get_http_method,response,
                        returnjson,redirect_url,set_cookie,get_cookie,del_cookie)
from django.urls import converters  #导入转换器
from django.urls import register_converter

# 自定义转换器
class DateConverter:
    regex = "\d{4}-\d{2}-\d{2}"  #正则
    def to_python(self, value):
        return value
    def to_url(self, value):
        return value

#注册转换器
register_converter(DateConverter, 'date')


urlpatterns = [
    path('index/',index),
    path('<int:shop_id>/<date:goods_id>/',goods), #使用转换器
    path('get_header/',get_header),
    path('get_http_method/',get_http_method),
    path('response/',response),
    path('returnjson/',returnjson),
    path('redirect_url/',redirect_url),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('del_cookie/',del_cookie),
]
