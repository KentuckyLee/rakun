from django.urls import path
from parents import views


app_name = "parents"

urlpatterns = [
    path('', views.index, name="index"),
    path('set_new_parent/', views.set_new_parent, name="set_new_parent"),
    path('get_profile/<str:id>/', views.get_profile, name="get_profile"),
    ]