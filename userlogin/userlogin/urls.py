from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', views.sign_up, name = 'signin1'),
    path('log_in/', views.log_in, name = 'login1'),
    path('user_profile/', views.user_profile, name = 'profile1'),
    path('logout_user/', views.user_logout, name = 'logout1'),
]
