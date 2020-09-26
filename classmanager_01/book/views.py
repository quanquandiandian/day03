from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def goods(request,cat_id,mobile):
    # print(cat_id,goods_id)
    print(cat_id,mobile)

    return HttpResponse('ok')