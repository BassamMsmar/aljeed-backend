from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from rest_framework import routers

from accounts import api
router = routers.DefaultRouter()
router.register('', api.UsersListApi)



urlpatterns = [
    path ('login/',  LoginView.as_view(template_name='accounts/login.html'), name="login" ),
    path ('logout/',  LogoutView.as_view(), name="logout" ),

    # api
    path('api/list/', include(router.urls), name='users_list_api'),

 
    ]
