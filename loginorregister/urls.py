from django.urls import path
from loginorregister import views


app_name = "loginorregister"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]