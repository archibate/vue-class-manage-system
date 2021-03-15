from django.contrib.auth import authenticate
from django.shortcuts import render
from django.views import View
from rest_framework.mixins import *
from .models import *
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, request, response
from django.core import serializers
import json
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import *

# Create your views here.

class Users(CreateModelMixin, ListModelMixin,GenericAPIView):
    queryset = User.objects.all()  # 指定当前类视图使用的查询集数据
    serializer_class = Userserializer  # 指定当前类视图使用的序列化器

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
# class LoginView(View):
#     def get(self, request):
#         #获取参数
#         user_id = request.GET.get('user_id')
#         password = request.GET.get('password')
#         if not all([user_id, password]):
#             return JsonResponse({'code': 400, 'msg': '帐号或密码不能为空'})
#         #验证参数并返回相应
#         user = authenticate(user_id=user_id, password=password)
#         if user is None:
#             return JsonResponse({'code': 400,'msg':'账号或密码错误'})
#         # if user_id == '15068091832' and password == '123456':
#         else:
#             return JsonResponse({'code': 200, 'msg': 'ok', 'info': {'user_id': user_id, 'user_name': 'black'}})
#
#         # 获取参数
#         data = json.loads(request.body.decode())
#         user_id = request.GET.get('user_id')
#         password = data.get('password')
#         if not all([user_id, password]):
#             return JsonResponse({'code': 400, 'msg': '帐号或密码不能为空'})
#         # 验证参数并返回相应
#         # if user_id == '15068091832' and password == '123456':
#         #     return JsonResponse({'code': 200, 'msg':'ok','info': {'user_id': user_id, 'user_name': 'black'}})
#         # else:
#         #     return JsonResponse({'code': 400,'msg':'账号或密码错误'})
#         user = authenticate(user_id=user_id, password=password)
#         if user is None:
#             return JsonResponse({'code': 400,
#                                  'msg': '账号或密码错误'})
#         # if user_id == '15068091832' and password == '123456':
#         else:
#             return JsonResponse({'code': 200, 'msg': 'ok',
#                                  'info': {'user_id': user_id, 'user_name': 'black'}})

# def jwt_response_payload_handler(token,user = None,request=None):
#     return {
#         'token':token,
#         'user':user.username,
#         'id':user.id,
#     }
