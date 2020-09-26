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
# request.body返回bytes类型
# json形式的字符串转换为Python字典   json.loads()
import json
def post_json(request):
    json_str = request.body
    json_str = json_str.decode()
    json_data=json.loads(json_str)
    # print(json_data['name'])
    # print(json_data['age'])
    # ji
    # 1
    # [26 / Sep / 2020 14: 50:14] "POST /post_json/ HTTP/1.1"

    print(json_data)
    # {'name': 'ji', 'age': 1}
    print(type(json_data))
    # <class 'dict'>

    # body=request.body
    # print(body)
    # b'{\n\t"name":"ji",\n\t"age":1\n}'



##########请求头
    print(request.META)
    # {'PATH': '/home/ubuntu/.virtualenvs/py3_django/

##############其他常用对象属性
def method(request):
    print(request.method)
    # GET/POST
    return HttpResponse('ok')


##############HttpResponse
# HttpResponse(content=响应体,content_type=响应体数据类型,status=状态码)
from django.http import HttpResponse
def response(request):
    return HttpResponse('itcast python',status=400)













