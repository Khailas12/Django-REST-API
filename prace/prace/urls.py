from django.contrib import admin
from django.urls import path, include
from .views import Practice
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', Practice.as_view(), name='practice'),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain')
]