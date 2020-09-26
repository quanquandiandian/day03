from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def goods(request,cat_id,goods_id,mobile):
    # print(cat_id,goods_id)

    print(cat_id,mobile)

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


##################json
# 非表单请求体数据使用  request.body  获取原始请求体数据 自己解析
# request.body  返回bytes类型
# 要获得请求体中{"a":1,"b":2}的json数据


import json

def post_json(request):
    json_str = request.body
    json_str=json_str.decode
    rep_data = json.loads(json_str)
    print(rep_data['a'])
    print(rep_data['b'])
    return HttpResponse('ok')


########验证path中路由参数
# int:

###############################自定义转换器

###请求头
def get_headers(request):
    print(request.META['HTTP_HOST'])
    return HttpResponse('ok')


#############其他请求对象
def methon(request):
    print(request.method)    #得到字符串‘ＧＥＴ’　‘ＰＯＳＴ’
    return HttpResponse('ok')

#####################HttpResponse對象
# HttpResponse(content=响应体,content_type=响应体数据类型,status=状态码)
from django.http import HttpResponse

def response(request):
    response=HttpResponse('itcast python',status=200)
    response['itcast']='python'
    return response
















