# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 11:48
# @Author  : super_kun
# @File    : views.py
# @Software: PyCharm
# @Desc    :
# from django.views import View
# from print import cats_classify as ts
# from django.http import HttpResponse
#
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from print import cats_classify as ts

# def load(request):
#     if request.method == "POST":
#         # 获取上传的文件，如果没有文件，则默认为None
#         File = request.FILES.get("myfile", None)
#         print(type(File))
#         personid = File.name[0:3]
#         if File is None:
#             return HttpResponse("没有需要上传的文件")
#         else:
#             # 打开特定的文件进行二进制的写操作
#             # print(os.path.exists('/temp_file/'))
#
#             if not os.path.exists("./temp_file/%s"%personid):
#                 os.makedirs("./temp_file/%s"%personid)
#                 with open("./temp_file/%s"%(personid+'/'+File.name), 'wb+') as f:
#                  for chunk in File.chunks():
#                     f.write(chunk)
#             else:
#                 with open("./temp_file/%s"%(personid+'/'+File.name), 'wb+') as f:
#                  for chunk in File.chunks():
#                     f.write(chunk)
#             result = ts("./temp_file/%s"%(personid+'/'+File.name))
#             print(result)
#             context = {"info": result}
#             return render(request,"web/info.html", context)
#                 # print(result)
#                 # return JsonResponse(data={"result": result})
#     else:
#         # return HttpResponse("哎呀出问题了")
#          return render(request, "web/load1.html")






@csrf_exempt
def load(request):
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("file", None)
        print(type(File))
        picturename=File.name
        print(picturename)
        username=request.POST.get('user')

        # username=request.FILES.get("formData")
        print(picturename)
        print(username)
        personid = File.name[0:3]
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            # 打开特定的文件进行二进制的写操作
            # print(os.path.exists('/temp_file/'))

            if not os.path.exists("temp_file/%s"%personid):
                os.makedirs("temp_file/%s"%personid)
                with open("temp_file/%s"%(personid+'/'+File.name), 'wb+') as f:
                 for chunk in File.chunks():
                    f.write(chunk)
            else:
                with open("temp_file/%s"%(personid+'/'+File.name), 'wb+') as f:
                 for chunk in File.chunks():
                    f.write(chunk)

                result = ts("temp_file/%s"%(personid+'/'+File.name))
                # image1 = image.objects.create(
                #     image=File,
                #     user_name=newapp.objects.get(name=username),
                #     filename=picturename,
                #     diagnose_result=result,
                # )
                # print(image1)
                print(result)
                context={"info": result}
                # return HttpResponse(result)
                return JsonResponse(data={"result": result})
    else:
        return JsonResponse({
            "result":"no"
        })




