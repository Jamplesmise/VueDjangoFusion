from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserLoginSerializer
from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.http import JsonResponse
@csrf_exempt
def test_view(request):
    return JsonResponse({'message': 'It works!'})

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # 打印请求数据
        return super().create(request, *args, **kwargs)


# 创建登录视图
class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username, password)

            # 使用默认的 authenticate 方法
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # 这里可以添加生成令牌的代码
                return Response({'message': '登录成功'}, status=status.HTTP_200_OK)
            else:
                print("用户名或密码验证失败")
                print("提取的用户名:", serializer.validated_data['username'])
                print("提取的密码:", serializer.validated_data['password'])
                return Response({'message': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_protect
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})
