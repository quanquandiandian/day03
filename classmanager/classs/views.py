from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def goods(request,cat_id,goods_id):
    print(cat_id,goods_id)
    return HttpResponse('ok')