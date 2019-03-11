from django.urls import path
from personnel import views


app_name = "personnel"

urlpatterns = [
    path('', views.index, name="index"),
    path('set_new_personnel/', views.set_new_personnel, name="set_new_personnel"),
]