from django.db import models


# Create your models here.
# article
class Article(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  content = models.TextField()
  # 封面图片
  cover = models.CharField(max_length=255)
  # 作者, 外键 User
  author = models.ForeignKey('users.UserProfileModel', on_delete=models.CASCADE)
  # 状态
  status = models.IntegerField(default=0)
  # 创建时间
  create_time = models.DateTimeField(auto_now_add=True)
  # 更新时间
  update_time = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'article'
    verbose_name = '文章'
    verbose_name_plural = '文章'

  def __str__(self):
    return self.title
