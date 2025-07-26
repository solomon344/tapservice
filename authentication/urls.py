from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import MyTokenObtainPairView, LoginView, EntryPoint


urlpatterns = [
    path('', EntryPoint.as_view(), name='entry-point'),
    path('login',LoginView.as_view(), name='login_view'),
    path('token',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh',TokenRefreshView.as_view()), 
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

]  