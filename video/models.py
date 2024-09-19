from django.db import models

# Create your models here.
# coding = utf-8
"""
    @project: missionPlatform
    @Author：Waite0603
    @file： models.py
    @date：2024/8/25 下午5:15

    TODO:
"""
from django.db import models


# 上传记录表格
class UploadRecord(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  # 文件路径
  path = models.FilePathField(path='upload/video', max_length=255)
  # 格式
  format = models.CharField(max_length=255)
  # 大小
  size = models.IntegerField()
  # 上传时间
  upload_time = models.DateTimeField(auto_now_add=True)
  # 上传者
  author = models.ForeignKey('users.UserProfileModel', on_delete=models.CASCADE)
  # 状态, 0: 被清理, 1. 正常, 2. 未被使用
  status = models.IntegerField(default=1)

  class Meta:
    db_table = 'upload_record'
    verbose_name = '上传记录'
    verbose_name_plural = '上传记录'
