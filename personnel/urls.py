from django.urls import path
from personnel import views


app_name = "personnel"

urlpatterns = [
    path('', views.index, name="index"),
    path('set_new_personnel/', views.set_new_personnel, name="set_new_personnel"),
    path('get_profile/<str:id>/', views.get_profile, name="get_profile"),
    path('personnel_update/<str:id>/', views.get_profile, name="personnel_update"),
    path('personnel_delete/<str:id>/', views.get_profile, name="personnel_delete"),
]