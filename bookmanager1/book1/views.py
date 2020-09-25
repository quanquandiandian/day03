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
###############################
















































