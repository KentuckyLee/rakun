from django.urls import path
from personnel import views


app_name = "personnel"

urlpatterns = [
    path('', views.index, name="index"),
    path('set_new_personnel/', views.set_new_personnel, name="set_new_personnel"),
    path('get_profile/<str:pers_id>/', views.get_profile, name="get_profile"),
    path('personnel_update/<str:pers_id>/', views.personnel_update, name="personnel_update"),
    path('account_update/<str:pers_id>/', views.account_update, name="account_update"),
    path('personnel_delete/<str:id>/', views.get_profile, name="personnel_delete"),
]