from django.urls import path
from classs.views import goods,get,post

urlpatterns = [
    path('<cat_id>/<goods_id>',goods),
    path('get/',get),
    path('post/',post),

]