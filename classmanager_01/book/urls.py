from django.urls import path, register_converter
from book.views import goods,get,post,post_json,method
from book.views import response

# 1.
class MobileConverter():
    # 正则检测
    regex='1[3-9]\d{9}'

    def to_python(self,value):
        return value


# 2.
register_converter(MobileConverter,'phone')

urlpatterns=[
    # path('<cat_id>/<goods_id>/',goods)
    path('<int:cat_id>/<phone:mobile>/',goods),
    path('get/',get),
    path('post/',post),
    path('post_json/',post_json),
    path('method/',method),
    path('response/',response),
]