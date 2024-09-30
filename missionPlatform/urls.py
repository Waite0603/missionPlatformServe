from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView,
)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('auth/', include('users.urls'), name='auth'),  # 用户模块
  path('video/', include('video.urls'), name='video'),  # 视频模块
  path('article/', include('article.urls'), name='article'),  # 文章模块
  path('course/', include('course.urls'), name='course'),  # 课程模块
  path('comment/', include('comment.urls'), name='comment'),  # 评论模块
  # # JTW认证接口
  # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # # 刷新JWT有效期接口
  # path('api/refresh', TokenRefreshView.as_view(), name='token_refresh'),
  # # 验证token有效期接口
  # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]
