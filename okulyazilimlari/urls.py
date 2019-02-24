from django.urls import path
from okulyazilimlari import views


app_name = "okulyazilimlari"

urlpatterns = [
    path('', views.index, name="index"),
]