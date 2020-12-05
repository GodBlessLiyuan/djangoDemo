from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context = {}
    # context['hello'] = 'Hello World!'
    # return render(request, 'runoob.html', context)
    # 单个值
    views_name = "菜鸟教程"
    # 数组是list
    # views_list=["","",""]
    # 字典或者对象
    views_dict={"name":"value","age":""}
    return render(request, "runoob.html", {"hello": views_name})