from django.urls import path
from notifications import views


app_name = "notifications"

urlpatterns = [
    path('', views.index, name="index"),
    path('send_notifications', views.send_notifications, name="send_notifications"),
    ]
