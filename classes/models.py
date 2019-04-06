from django.db import models

# Create your models here.


class Classes(models.Model):
    company_id = models.CharField(max_length=40)
    class_name = models.CharField(max_length=50)
    quota = models.IntegerField()
    registered_student = models.IntegerField()
    status_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Güncelleme tarihi
