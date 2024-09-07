from django.db import models


# Create your models here.
# 课程
class Course(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, verbose_name='课程名称')
  desc = models.CharField(max_length=200, verbose_name='课程描述')
  cover = models.CharField(max_length=100, verbose_name='封面')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
  update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
  category = models.ForeignKey('CourseCategory', on_delete=models.CASCADE, verbose_name='所属分类')
  # 状态, 0: 被清理, 1. 正常
  status = models.IntegerField(default=1)
  # 创建者
  author = models.ForeignKey('users.UserProfileModel', on_delete=models.CASCADE)

  class Meta:
    db_table = 'course'
    verbose_name = '课程'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name


# 章节
class Chapter(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, verbose_name='章节名称')
  course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='所属课程')
  video = models.CharField(max_length=100, verbose_name='视频')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
  update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
  watch_num = models.IntegerField(default=0, verbose_name='观看次数')
  author = models.ForeignKey('users.UserProfileModel', on_delete=models.CASCADE)
  # 状态, 0: 被清理, 1. 正常, 2. 未被使用
  status = models.IntegerField(default=1)

  class Meta:
    db_table = 'course_chapter'
    verbose_name = '章节'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name


class CourseCategory(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50, verbose_name='分类名称')
  desc = models.CharField(max_length=200, verbose_name='分类描述')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
  update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

  class Meta:
    db_table = 'course_category'
    verbose_name = '课程分类'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name
