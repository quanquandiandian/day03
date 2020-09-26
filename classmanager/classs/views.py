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
"""
第一次请求,   携带  查询字符串 
http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器接收到请求之后  获取username  服务器设置cookie信息,cookie信息包括username
浏览器接收到服务器的响应之后 应该把cookie保存起来

第二次及其之后的请求,,我们访问http://127.0.0.1:8000  都会携带cookie信息
"""



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
#     response.delete_cookie('itcast1')

############session
"""
第一次请求  http://127.0.0.1:8000/set_session/?username=itheima
我们在服务器端设置session信息
服务器同时会生成一个session_id的cookie信息
浏览器接收到这个信息之后,会把cookie数据保存起来

第二次及其之后的请求  都会携带这个session_id  服务器会验证这个session_id
验证没有问题会读取相关数据,实现业务逻辑


"""
def set_session(request):
#     1.模拟  获取用户信息
    username=request.GET.get('username')
# 2.设置session信息
# 假如  通过模型查询到用户信息
    user_id=1

    request.session['user_id']=user_id
    request.session['username']=username


#   clear 删除session里的数据  保留key
#   request.session.clear()
#   flush  是删除所有数据  包括key
#   request.session.flush()
    request.session.set_expiry(3600)   #设置失效时间
    return HttpResponse('ok')

def get_session(request):

    username=request.session.get('username')
    user_id=request.session.get('user_id')

    content='{},{}'.format(username,user_id)
    return HttpResponse(content)

###################类视图
def register(request):
    """处理注册"""
    # 获取请求方法,判断是GET/POST请求
    if request.method == 'GET':
#       处理GET请求, 返回注册页面
        return render(request,'register.html')
    else:
#         处理POST请求  实现注册逻辑
        return HttpResponse('这里是实现注册逻辑')

#########类视图使用
from django.views.generic import View
class RegisterView(View):
#     类视图:处理注册
    def get(self,request):
#       处理get请求  返回注册页面
        return render(request,'register.html')
    def post(self,request):
#         处理POST请求,实现注册逻辑
        return HttpResponse('这里实现注册逻辑')


























