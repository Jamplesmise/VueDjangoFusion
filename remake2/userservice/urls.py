from django.urls import path
from .views import RegisterView, LoginView, test_view, logout_view

urlpatterns = [
    path('api/test/', test_view, name='test'),
    # 添加注册路由
    path('register/', RegisterView.as_view(), name='register'),
    # 添加登录路由
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

]
