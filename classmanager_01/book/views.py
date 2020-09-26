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
    # a=request.POST.get('a')
    # b=request.POST.get('b')
    # alist=request.POST.getlist('a')
    # print(a)
    # print(b)
    # print(alist)
    data=request.POST
    print(data)
    # < QueryDict: {'user': ['1'], 'password': ['123']} >设置key/v否则返回none/[]
    return HttpResponse('ok')


########################json
import json
def post_json(request):
    json_str = request.body
    json_str = json_str.decode()
    json_data=json.loads(json_str)
    print(json_data['name'])
    print(json_data['age'])
    print(type(json_data))
    # ji
    # 1
    # [26 / Sep / 2020 14: 50:14] "POST /post_json/ HTTP/1.1"


    # body=request.body
    # print(body)
    # b'{\n\t"name":"ji",\n\t"age":1\n}'


    return HttpResponse('ok')


















