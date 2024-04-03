from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.signup, name='signup'),
    path('', views.success, name='success'),
    path('', views.user_login, name='login'),
    path('', views.index, name='index'),
]