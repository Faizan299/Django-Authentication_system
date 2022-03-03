from django import views
from django.urls import path,include
from .views import login, signup,logout,custom_password_reset
from . import views



urlpatterns = [
    path('login/', login, name='login' ),
    path('register/', signup, name='register' ),
    path('logout/',logout,name="logout"),
    path('password-reset/', custom_password_reset, name='password-reset' ),
    path('', include('django.contrib.auth.urls')),
    
    
    
]
