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


class Video(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  description = models.TextField()
  # 封面图片
  cover = models.CharField(max_length=255)
  # 视频地址
  video = models.CharField(max_length=255)
  # 上传时间
  upload_time = models.DateTimeField(auto_now_add=True)
  # 点赞数
  like = models.IntegerField(default=0)
  # 评论数
  comment = models.IntegerField(default=0)
  # 观看数
  watch = models.IntegerField(default=0)
  # 作者, 外键 User
  author = models.ForeignKey('users.UserProfileModel', on_delete=models.CASCADE)
  # 分类, 外键 Category
  category = models.ForeignKey('video.Category', on_delete=models.CASCADE)
  # 状态
  status = models.IntegerField(default=0)

  class Meta:
    db_table = 'video'
    verbose_name = '视频'
    verbose_name_plural = '视频'

  def __str__(self):
    return self.title


class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  # 分类描述
  description = models.TextField()
  # 分类封面
  cover = models.CharField(max_length=255)
  # 创建时间
  create_time = models.DateTimeField(auto_now_add=True)
  # 状态
  status = models.IntegerField(default=0)

  class Meta:
    db_table = 'category'
    verbose_name = '分类'
    verbose_name_plural = '分类'

  def __str__(self):
    return self.name


# 上传记录表格
class UploadRecord(models.Model):
  id = models.AutoField(primary_key=True)
  # 路径
  path = models.CharField(max_length=255)
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
