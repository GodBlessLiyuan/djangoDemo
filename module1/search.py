from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
# 表单
from django.views.decorators.csrf import csrf_exempt


def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
# 它相当于控制器和业务处理器了；只是没有包含路径配置；
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

@csrf_exempt
def savefile(request):
    print(request.method)
    if request.method == 'POST':
        f = request.FILES['picture']
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT,0o666)
        filepath = os.path.join(settings.MEDIA_ROOT, f.name)
        print(filepath)
        with open(filepath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
            fp.close()
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')