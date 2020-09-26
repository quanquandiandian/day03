from django.shortcuts import render, redirect
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
from django.http import HttpResponse,JsonResponse

def response(request):
    # response=HttpResponse('itcast python',status=200)
    # response['itcast']='python'
    # return response

#############dict>>>>>>json
    girls=[
        {
            'name':'rose',
            'address':'shunyi'
        },
        {
            'name':'jack',
            'address':'changping'
        }
    ]
#     data返回的相应数据一般是字典类型
    """
    safe=Ture   是表示data是字典数据
    JsonResponse  可以吧字典转化为json
    
    现在是非字典  改为Falue
    
    """

    # response=JsonResponse(data=girls,safe=False)

    # return response
#######重定向
    # return redirect('/get_headers')
#####################cookie

# 设置cookie
# HttpResponse.set_cookie(cookie名,value=cookie值,max_age=cookie有效期)
def set_cookie(request):
    response =HttpResponse('ok')
    response.set_cookie('itcast','python1')#临时cookie
    response.set_cookie('itcast1','python2',max_age=60*60)
    return response



# 读取cookie
def get_cookie(request):
    cookie1 = request.COOKIES.get('itcast')
    print(cookie1)
    return HttpResponse('ok')

# 删除cookie
    response.delete_cookie('itcast1')


