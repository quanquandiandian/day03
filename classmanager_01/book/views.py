from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def goods(request,cat_id,mobile):
    # print(cat_id,goods_id)
    print(cat_id,mobile)

    return HttpResponse('ok')


##########查询字符串
# http://127.0.0.1:8000/get/?a=1&b=2&a=3
def get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)   #3
    print(b)  #2
    print(alist)   #['1','3']
    return HttpResponse('ok')

###################form


# 通过request.POST属性获取  返回QueryDict对象
def post(request):
    a=request.POST.get('a')
    b=request.POST.get('b')
    alist=request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('ok')







