from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django.urls import path

from accounts.view.auth import CustomUserCreateAPIView, CustomUserListAPI, CustomUserDetailAPI, CustomUserUpdateAPI, \
    CustomUserDeleteAPI
from accounts.view.profile import ProfileDetailAPIView, ProfileUpdateAPIView, ProfileDeleteAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # register url
    path("user/",CustomUserCreateAPIView.as_view(),name="user"),
    path('user/list/',CustomUserListAPI.as_view(),name="user_list"),
    path('user/detail/<int:pk>/',CustomUserDetailAPI.as_view(),name="user_detail"),
    path('user/update/<int:pk>/',CustomUserUpdateAPI.as_view(),name="user_update"),
    path('user/delete/<int:pk>/',CustomUserDeleteAPI.as_view(),name="user_delete"),

    # profile url

    path('profile/',ProfileDetailAPIView.as_view(),name="profile_detail"),
    path('profile/update/',ProfileUpdateAPIView.as_view(),name="profile_update"),
    path('profile/delete/',ProfileDeleteAPIView.as_view(),name="profile_delete"),

]