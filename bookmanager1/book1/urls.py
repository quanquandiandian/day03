from django.urls import path
from django.urls.converters import register_converter
from django.urls import converters

from book1.views import player, register, json, method,response


# 1.定义转换器
class MobileConverter:
# 验证数据的关键是：正则
    regex = '1[3-9]\d{9}'

#     验证没有问题的数据，给视图函数
    def to_python(self,value):
        return value

# def to_url(self,value):

# 将匹配结果用于反向解析传值时使用
# return value

# 2.先注册转换器，才能在第三部使用
# converter 转换器类
# type_name  转换器名字
register_converter(MobileConverter,'phone')
########################定义转换器
# class MobileConverter:
#     regex = '1[3-9]\d{9}'
#
#     def to_python(self, value):
#         return value
#
#
# register_converter(MobileConverter, 'phone')

urlpatterns = [
    # <转换器名字：变量名>
    # 转换器会对变量数据进行正则的验证
    path('<int:team_id>/<phone:mobile>/',player),
    # path('<int:city_id>/<phone:mobile>', shop),

    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('res/', response),


]

"""

class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
"""



