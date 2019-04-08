from django.db import models

# Create your models here.

class Parents(models.Model):
    ### Personnel data

    user_name = models.CharField(max_length=50, null=False)  # Kullanıcı İsmi
    user_surname = models.CharField(max_length=50, null=False)  # Kullanıcı İsmi
    phone_number = models.CharField(max_length=10)  # Telefon numarası
    mail = models.CharField(max_length=150, null=True)  # Kullanıcı adresi
    birth_date = models.DateTimeField(auto_now_add=False, null=False)  # Kullanıcının doğu tarihi
    address = models.TextField(null=True)  # Adres bilgisi
    company_id = models.CharField(max_length=40)  # owner kulanıcının telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    category_id = models.CharField(null=False, max_length=50)  # Kullanıcı kategorisi
    students_count = models.IntegerField(null=False)
    status_id = models.IntegerField(default=2)  # Kullanıcı statusu
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Güncelleme tarihi
