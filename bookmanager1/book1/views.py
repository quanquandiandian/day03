from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def player(request,team_id,player_id):
    # 使用路径参数
    # print(team_id,player_id)


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
















































