from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def myget(request):
    return HttpResponse(request.GET.get("name"))
#form表单的请求
@csrf_exempt
def mypost(request):
    print(request.POST.get("name"))
    return HttpResponse(request.POST.get("name"))

# 比如二进制图片，xml,json
# 好像是不需要参数的
@csrf_exempt
def mybinary(request):
    # print(request.body)#可以将二进制转为图片
    # print(request.headers)
    print(request.content_params)
    return HttpResponse("binary")
# /mypathOrUrl
# http://127.0.0.1:8000/mypathOrUrl?name=haha
# /mypathOrUrl
# http://127.0.0.1:8000/mypathOrUrl?name=haha
@csrf_exempt
def mypathOrUrl(request):
    print(request.path)
    # print(request.get_raw_uri())
    return HttpResponse("path url区别")

# @这个相当于@restController
def mymethod(request):
    name = request.method
    print(name)
    return HttpResponse("method")
    #HttpResponse可以理解为json格式

# 这个相当于@controller,携带了页面
# 不要试path和url区别了
# @csrf_exempt # postman需要添加

def myrender(request):
    hello={"name":"dasha","age":27}
    print("render")
    return render(request,"runoob.html",{"varname":hello})
def myredirect(request):
    return redirect("/runoob.html")
