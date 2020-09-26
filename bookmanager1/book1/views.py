from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
def player(request,team_id,mobile):
    # 使用路径参数
    # print(team_id,player_id)
    print(team_id,mobile)











    # 得到QueryDict对象
    # query_params=request.GET
    # print(query_params)

    # 一键多值
    # order=query_params.getlist('order')
    # print(order)
    return HttpResponse('湖人总冠军！')

############
"""
查询字符串
http://ip:port/path/path?key=value&key1=value1

url  以?为分割  分为2部分
？前边为  请求路径
？后边为   查询字符串  查询字符串  类似于字典  key=value  多个数据采用&拼接
"""
# ###########查询字符串Query String#########
# /get/?a=1&b=2&a=3
# def get(request):
#     a = request.GET.get('a')
#     b = request.GET.get('b')
#     alist = request.GET.getlist('a')
#     print(a)
#     print(b)
#     print(alist)
#     return HttpResponse('ok')
#
###########请求体####################
# form表单
def register(request):
    data=request.POST
    print(data)
    # <QueryDict: {'username':['itcast'],'password':['123']}>
    return HttpResponse('ok!')

# Json
def json(request):
    # request.Post    json数据不能通过   request.Post获取数据
    body_str=request.body
    # print(body)
    # b'{\n\t           "name":"itcast"\n\t\t\t\t"age":10\n}'



    # body_str=body.decode()
    # print(body_str)
    """
    {
                   "name":"itcast"
                    "age":10
    }    <class 'str'>
    """


    # json形式的字符串可以转换为Python的字典
    import json
    body_dict=json.loads(body_str)
    # print(body_dict)
    # {'name': 'itcast', 'age': 10}


########################请求头
    # print(request.META)
    # print(request.META['SERVER_PORT'])
    return HttpResponse('ok')

####################其他常用HttpRequest对象属性
def method(request):
    print(request.method)
    return HttpResponse('ok')


#############自定义转换器
# def shop(request,city_id,mobile):
#     print(city_id,mobile)
#     return HttpResponse('ok')



#####################HttpResponse对象
def response(request):
    # return HttpResponse('ok',status=500)
    #1xx
    #2xx   200  ok
    #3xx
    #4xx   请求有问题
    # 403    Forbidden   禁止访问   权限有问题
    # 404    NotFound     找不到页面  路由有问题
    # 405    Method Not
    #5xx

# #######设置响应头
    response=HttpResponse('ok')

    response['name']='itcast'

    return response

###########HttpResponse子类
# from django.http import HttpResponse,HttpResponseNotFound


############JsonResponse
from django.http import HttpResponse,JsonResponse
def response(request):
    # dict>>>>>>Json

    infos=[
        {
            'name':'ku',
            'address':'123456'
        },
        {
            'name':'hdaho',
            'hsdi':'ndkasdf'
        }
    ]
    # data  返回的相应数据   一般是字典类型
    """
    safe = True 是表示  data是字典数据
    JsonResponse  可以吧字典转化为json
    现在是非字典数据，出问题自己负责 
    """


    response =JsonResponse(data=infos,safe=False)

    # return response


###########重定向
    return redirect('http://www.baidu.com')








































