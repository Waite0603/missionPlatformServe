from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfileModel(AbstractUser):
  """
  创建一个用户的模型
  """
  SEX_CHOICES = [
    ('male', '男'),
    ('female', '女')
  ]
  phone = models.CharField(max_length=11, verbose_name='手机号', unique=True)
  birthday = models.DateField(verbose_name='生日', null=True, blank=True)
  sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='', verbose_name='性别')
  # 头像
  avatar = models.CharField(max_length=100, default='default.jpg', verbose_name='头像')
  address = models.CharField(max_length=100, default='', verbose_name='地址')

  class Meta(object):
    db_table = 'user_profile'
    verbose_name = '用户信息'
    verbose_name_plural = verbose_name

  def __str__(self):
    # 定义模型对象的显示信息
    return self.username


# 联系我们表单
class Contact(models.Model):
  name = models.CharField(max_length=50, verbose_name='姓名')
  email = models.EmailField(max_length=50, verbose_name='邮箱')
  message = models.TextField(verbose_name='留言')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

  class Meta:
    db_table = 'contact'
    verbose_name = '联系我们'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name