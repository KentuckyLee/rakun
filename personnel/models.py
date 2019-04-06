from django.db import models

# Create your models here.
# Users model

class Personnels(models.Model):

    ### Personnel data
    user_name = models.CharField(max_length=50)  # Kullanıcı İsmi
    user_surname = models.CharField(max_length=50)  # Kullanıcı İsmi
    mail = models.CharField(max_length=150, null=True)  # Kullanıcı adresi
    image_url = models.FileField(blank=True, null=True)  # Kullanıcı profil resmi
    birth_date = models.DateTimeField(auto_now_add=False, null=False)  # Kullanıcının doğu tarihi
    address = models.TextField(null=True)  # Adres bilgisi
    university = models.CharField(max_length=120, null=True)  # Üniversite bilgisi

    ### Personnel authenticate data
    phone_number = models.CharField(max_length=10)  # Telefon numarası
    company_id = models.CharField(max_length=40)  # owner kulanıcının telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    class_room = models.CharField(max_length=80)  # personelin sorunlu olduğu derslik
    personnel_type = models.IntegerField(null=False)  # personelin kurumda görevlendirildiği pozisyon
    category_id = models.IntegerField(null=False)  # Kullanıcı kategorisi
    status_id = models.IntegerField(default=2)  # Kullanıcı statusu
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Güncelleme tarihi





