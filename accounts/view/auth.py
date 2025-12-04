from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from ..models import CustomUser
from ..serializers.user import CustomUserListSerializer, CustomUserCreateSerializer, CustomUserDetailSerializer


class CustomUserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer




class CustomUserListAPI(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer


class CustomUserDetailAPI(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer

class CustomUserUpdateAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer


class CustomUserDeleteAPI(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer