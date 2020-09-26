from django.urls import path
from classs.views import goods

urlpatterns = [
    path('<cat_id>/<goods_id>',goods)

]