
from django.contrib import admin
from django.urls import path, re_path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/',include('authentication.urls'))
]
