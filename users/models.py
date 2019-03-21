from django.db import models

# Create your models here.


class TestUsers(models.Model):

    company_id = models.CharField(max_length=50)  # Anaokulu id' si
    company = models.CharField(max_length=50)  # Anaokulu ismi
    phone_number = models.CharField(max_length=10)  # Telefon numarası
    password = models.CharField(max_length=20)  # Kullanıcı Şifresi
    category_id = models.IntegerField()  # Kategori id' si
    user_name = models.CharField(max_length=20)  # Kullanıcı ismi
    user_surname = models.CharField(max_length=50)  # Kullanıcı Soyismi
    mail = models.CharField(max_length=50)  # Kullanıcı mail adresi
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Güncelleme tarihi
    status_id = models.IntegerField()  # Status bilgisi
