from rest_framework import serializers
# serializers.ModelSerializer: 模型类序列化器基类
from .models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
        extra_kwargs = {
            'username':{'min_value':0},
            'mobile':{'min_value':0}
        }

    def validate(self, attrs):
        # 自定义校验
        return attrs