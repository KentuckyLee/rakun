from django.urls import path
from companies import views


app_name = "companies"

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('set_new_password/', views.set_new_password, name="set_new_password"),
]