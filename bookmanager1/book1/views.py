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
    # return redirect('http://www.baidu.com')



#############Cookie######################Session############
"""
第一次请求，携带  查询字符串
http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器接收到请求之后，获取username.服务器设置cookie信息，cookie信息包括  username
浏览器接收到服务器响应之后应该把cookie保存起来


第二次及其之后的请求，我们访问http://127.0.0.1:8000  都会携带cookie信息.  服务器就可以读取cookie信息，来判断用户身份

"""
def set_cookie(request):
#     1.获取查询字符串数据
    username=request.GET.get('username')
    password=request.GET.get('password')
#   2.服务器设置cookie信息
#   通过响应对象.set_cookie方法
    response=HttpResponse('set_cookie')
#   key, value=''
#   max_age 是一个秒数  从相应开始  计数的一个秒数
    response.set_cookie('name',username,max_age=60*60)
    response.set_cookie('pwd',password)

    # response.delete_cookie('name')

    return response


def get_cookie(request):
#     获取cookie

    print(request.COOKIES)
# request.COOKIE   字典数据
    name=request.COOKIES.get('name','pwd')
    return HttpResponse(name)

# ############################
"""
第一次请求，携带   查询字符串
http：//127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器同时会生成一个session——id的cookie信息
浏览器接收到这个信息之后，会把cookie数据保存下来



第二次及其之后的请求   都会携带这个session.  服务器会验证这个session.验证没有问题会读取相关数据.实现业务逻辑

"""


def set_session(request):

#     1.模拟  获取用户信息
    username=request.GET.get('username')

#     2.设置session信息
#       假如  我们通过模型查询  查询到了用户信息
    user_id=1

    request.session['user_id']=user_id
    request.session['user_name']=username




    #clear 删除session里的数据，保留key
    # request.session.clear()
    # flush 是删除所有数据
    # request.session.flush()
    request.session.set_expiry(3600)
    return HttpResponse('set_session')


#################类视图
def login(request):
    print(request.method)

    if request.method == 'GET':

        return HttpResponse('get  逻辑')
    else:

        return HttpResponse('POST 逻辑')

"""
类视图定义

class 类视图名字(view):

    def get(self,request)：
        return HttpResponse('xxx')

    def http_methon_lower(self,request):

        return HttpResponse('xxx')

1.继承自view
2.类视图中的方法  是采用http方法小写来区分不同的请求方式
"""
from django.views import View

class LoginView(View):
    def get(self,request):
        return HttpResponse('get get get')


    def post(self,request):
        return HttpResponse('post post post')




















