# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： serializer.py
    @date：2024/6/17 下午10:43

"""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import UserProfileModel

"""
  序列化器
"""


# 注册序列化器
class RegisterSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(label='确认密码', min_length=6, max_length=20, write_only=True,
                                           error_messages={
                                             'min_length': '密码长度不能小于6',
                                             'max_length': '密码长度不能大于20',
                                             'required': '密码不能为空'
                                           })

  class Meta:
    model = UserProfileModel
    fields = ('id', 'username', 'password', 'confirm_password', 'token', 'email', 'phone')

    # 为字段添加额外的校验规则
    extra_kwargs = {
      'username': {
        'label': '用户名',
        'min_length': 6,
        'max_length': 20,
        'error_messages': {
          'min_length': '用户名长度不能小于6',
          'max_length': '用户名长度不能大于20',
          'required': '用户名不能为空'
        }
      },
      'password': {
        'label': '密码',
        'min_length': 6,
        'max_length': 20,
        'write_only': True,
        'error_messages': {
          'min_length': '密码长度不能小于6',
          'max_length': '密码长度不能大于20',
          'required': '密码不能为空'
        }
      },
      'email': {
        'label': '邮箱',
        'write_only': True,
        'error_messages': {
          'required': '邮箱不能为空'
        },
        'validators': [
          UniqueValidator(queryset=UserProfileModel.objects.all(), message='邮箱已存在')
        ]
      },
      'phone': {
        'label': '手机号',
        'write_only': True,
        'error_messages': {
          'required': '手机号不能为空'
        }
      }
    }

  def validate(self, attrs):
    # 验证两次密码是否一致
    if attrs['password'] != attrs['confirm_password']:
      raise serializers.ValidationError('两次密码不一致')
    return attrs

  def create(self, validated_data):
    # 移除确认密码
    validated_data.pop('confirm_password')

    # 创建用户
    user = UserProfileModel.objects.create_user(**validated_data)

    return user