from django.urls import path, register_converter
from classs.views import goods,get,post,post_json,get_headers,method

# 1.定义转换器
class MobileConverter():
    # 验证数据的关键是：   正则
    regex = '1[3-9]\d{9}'

#     验证没有问题的数据，给视图函数
    def to_python(self,value):
        return value

# 2.注册转换器
# converter 转换器类
# type_name   转换器名字
register_converter(MobileConverter,'phone')




urlpatterns = [
    path('<int:cat_id>/<phone:mobile>',goods),
    # path('<int:cat_id>/<int:goods_id>',goods),



    path('get/',get),
    path('post/',post),
    path('post_json/',post_json),
    path('get_headers/',get_headers),
    path('method/',method),

]