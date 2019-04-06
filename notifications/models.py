from django.db import models

# Create your models here.
# Notification model

class Notifications(models.Model):

    created_user_id = models.CharField(max_length=4000)  # Oluşturan kullanıcının telefon numarası
    assigned_user_id = models.CharField(max_length=40000)  # Mesaj sahini telefon numarası
    company_id = models.CharField(max_length=50)  # Anaokulu ismi
    content = models.TextField()  # mesaj
    is_read = models.IntegerField()  # Okundu / okunmadı
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Oluşturuma tarihi

