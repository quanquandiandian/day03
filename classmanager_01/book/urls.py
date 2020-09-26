from book.views import goods
from django.urls import path


urlpatterns=[
    path('<cat_id>/<goods_id>/',goods)
]