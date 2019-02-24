from django.urls import path
from loginorregister import views


app_name = "loginorregister"

urlpatterns = [
    path('', views.index, name="index"),
]