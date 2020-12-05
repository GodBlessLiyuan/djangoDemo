"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# 导入视图的文件名，
from module1 import views,testdb,search,first,savefile
# 以方法为值，对应着url路径，
urlpatterns = [
    # 路径对应着view里面
    url('md1hello', first.hello),
    #返回带有页面信息的
    path('runoob', first.runoob),
    # 数据库操作
    path('testdb/', testdb.testdb),
    path('testdb/', testdb.testdbQuery),
    url(r'^search-form/$', search.search_form),
    # 相当于一个路径配置
    url(r'^search/$', search.search),
    url(r'^search_post/$', search.search_post),
    # 文件上传
    url(r'^savefile$', search.savefile),
    # url/path在postman中可以
    url("myget",views.myget),
    #path访问好使、url访问好使
    url("mypost",views.mypost),
    url("mybinary",views.mybinary),
    # 感觉不到区别
    path("mypathOrUrl",views.mypathOrUrl),
    # path好像没有返回
    path("myrender",views.myrender),
    path("myredirect",views.myredirect),
    path("faceReg",savefile.faceReg)
]
