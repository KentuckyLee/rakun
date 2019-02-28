from django.urls import path
from companies import views


app_name = "companies"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]