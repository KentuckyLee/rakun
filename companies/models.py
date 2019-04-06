from django.db import models

# Create your models here.

#  Register Model


class Companies(models.Model):

    phone_number = models.CharField(max_length=10)  # Telefon numarası
    # company_id = models.CharField(max_length=10)  # owner kullanıcının telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    user_name = models.CharField(max_length=50)  # Kurucu İsmi
    user_surname = models.CharField(max_length=50)  # Kurucu İsmi
    mail = models.CharField(max_length=50)  # Mail adresi
    credits = models.IntegerField()   # Satın alınan kredi
    credits_price = models.IntegerField()  # Ödenecek Tutar
    credits_price_date = models.DateTimeField(auto_now_add=False, null=True)  # Kredş satın alma tarihi
    credits_expiration_date = models.DateTimeField(auto_now_add=False)  # Kredinin sonlanma tarihi
    # country = models.CharField(max_length=30, blank=True, null=True)  # Ülke
    # city = models.CharField(max_length=30, blank=True, null=True)  # Şehir
    # district = models.CharField(max_length=30, blank=True, null=True)  # Semt
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Güncelleme tarihi
    # Kullanıcı statu bilgisi sisteme ilk kayıt olan kullanıcılar pasif statusunde kayıt edilir.
    status_id = models.IntegerField(default=2)




