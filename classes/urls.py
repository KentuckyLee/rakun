from django.urls import path
from classes import views


app_name = "classes"

urlpatterns = [
    path('', views.index, name="index"),
    path('set_new_class/', views.set_new_class, name="set_new_class"),
    path('update/<str:class_id>/', views.update, name="update"),
    path('update/', views.update, name="update"),
    path('delete/<str:class_id>/', views.delete, name="delete"),
    ]
