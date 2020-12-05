from django.conf import settings
from django.http import HttpResponse
from module1.svm_5 import reg_res
# 表单
from django.views.decorators.csrf import csrf_exempt
import os
@csrf_exempt
def faceReg(request):
    print(request.method)
    f = request.FILES['picture']
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT,0o666)
    filepath = os.path.join(settings.MEDIA_ROOT, f.name)
    print(filepath)
    with open(filepath, 'wb') as fp:
        for info in f.chunks():
            fp.write(info)
        fp.close()
    try:
        number=reg_res(filepath)
        os.remove(filepath)
        return HttpResponse(number)
    except IOError as err:
        print("recall error:{}".format(err))
        return HttpResponse("")