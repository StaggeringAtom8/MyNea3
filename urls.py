from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name= "register"),
    path('login/', views.loginPage, name= 'login' ),
    path('logout/', views.logout),
    path('', views.home, name="home"),
    path('progress/', views.progress, name='progress'),
    path('statistics/', views.statistics, name="statistics"),
]