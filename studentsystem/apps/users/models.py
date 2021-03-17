from django.contrib.auth.models import AbstractUser
from django.db import models
# from __future__ import unicode_literals

# Create your models here.

# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    username = models.CharField(max_length=50,unique=True,verbose_name='姓名')
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# Create your models here.
from django.shortcuts import render

#
# class UserInfo(AbstractUser):
#     """自定义用户模型类"""
#     mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
#
#     class Meta:
#         db_table = 'tb_users'
#         verbose_name = '用户'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username