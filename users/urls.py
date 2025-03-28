from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name= 'users'

urlpatterns =[

    path("register/", views.register_request, name="register"),
    path('', views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('home/', views.home, name='home'),

]