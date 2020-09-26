from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def goods(request,cat_id,goods_id):
    print(cat_id,goods_id)
    return HttpResponse('ok')

# 查询字符串Query  String
# 路径中有？key1=v1&k2=v2...  使用request.GET获取  返回Query String对象
# /get/?a=1&b=2&a=3
def get (request):
    a=request.GET.get('a')
    b=request.GET.get('b')
    alist=request.GET.getlist('a')
    print(a)   #3
    print(b)   #2
    print(alist)  #['1','3']
    return HttpResponse('ok')


# get('键',默认值)
# getlst('键',默认值)

############################
# form表单
# 前端发送的表单类型的请求体数据  通过request.POST获取  返回Query String对象

def post(request):
    a=request.POST.get('a')
    b=request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('ok')











