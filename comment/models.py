from django.db import models


# Create your models here.
# 评论
class CourseComment(models.Model):
  id = models.AutoField(primary_key=True)
  content = models.TextField(verbose_name='评论内容')
  create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
  update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
  # 状态, 0: 被清理, 1. 正常
  status = models.IntegerField(default=1)
  # 创建者
  author = models.ForeignKey('users.UserProfileModel', on_delete=models.CASCADE)
  # # 评论对象
  # target = models.ForeignKey('self', on_delete=models.CASCADE)
  # 评价课程
  course = models.ForeignKey('course.Course', on_delete=models.CASCADE)

  class Meta:
    db_table = 'course_comment'
    verbose_name = '评论'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.content
