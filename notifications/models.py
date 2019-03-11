from django.db import models

# Create your models here.
# Notification model

class TestNotifications(models.Model):

    created_user = models.IntegerField()  # Oluşturan kullanıcının telefon numarası
    assigned_user = models.IntegerField()  # Mesaj sahini telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    content = models.TextField()  # mesaj
    is_read = models.IntegerField()  # Okundu / okunmadı
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Oluşturuma tarihi

