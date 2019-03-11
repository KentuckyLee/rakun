from django.db import models

# Create your models here.
# Users model

class TestPersonnel(models.Model):

    ### Personnel data
    user_name = models.CharField(max_length=50)  # Kullanıcı İsmi
    user_surname = models.CharField(max_length=50)  # Kullanıcı İsmi
    mail = models.CharField(max_length=150, null=True)  # Kullanıcı adresi
    image_url = models.FileField(blank=True, null=True)  # Kullanıcı profil resmi
    birth_date = models.DateTimeField(auto_now_add=False, null=False)  # Kullanıcının doğu tarihi
    address = models.TextField(null=True)  # Adres bilgisi
    university = models.CharField(max_length=120, null=True)  # Üniversite bilgisi
    domain = models.CharField(max_length=120, null=True)  # Bolüm bilgisi
    language = models.CharField(max_length=120, null=True)  # Bildiği yabancı diller
    graduated_date = models.DateTimeField(auto_now_add=False, null=True)  # Mezuniyet yılı

    ### Personnel authenticate data
    phone_number = models.CharField(max_length=10)  # Telefon numarası
    password = models.CharField(max_length=16)  # Şifre
    company_id = models.CharField(max_length=10)  # owner kulanıcının telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    class_room = models.IntegerField(default=0)  # personelin sorunlu olduğu derslik
    position = models.IntegerField(null=False)  # personelin kurumda görevlendirildiği pozisyon
    category = models.IntegerField(null=False)  # Kullanıcı kategorisi
    status = models.IntegerField(default=2)  # Kullanıcı statusu
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Güncelleme tarihi





