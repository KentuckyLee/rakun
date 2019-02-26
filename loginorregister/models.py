from django.db import models

# Create your models here.

#  Register Model


class Test(models.Model):

    phone_number =models.CharField(max_length=10)  # Telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    password = models.CharField(max_length=16)  # Şifre
    owner = models.CharField(max_length=50)  # Kurucu İsmi
    mail = models.CharField(max_length=50)  # Mail adresi
    credit = models.IntegerField()   # Satın alınan kredi
    credits_price = models.IntegerField()  # Ödenecek Tutar
    credits_price_date = models.DateTimeField(auto_now_add=False)  # Kredş satın alma tarihi
    credits_expiration_date = models.DateTimeField(auto_now_add=False)  # Kredinin sonlanma tarihi
    image_url = models.FileField(blank=True, null=True)  # Owner profil resmi
    country = models.CharField(max_length=30, blank=True)  # Ülke
    city = models.CharField(max_length=30, blank=True)  # Şehir
    district = models.CharField(max_length=30, blank=True)  # Semt
    created_date = models.DateTimeField(auto_now_add=False)  # Kayıt tarih
    #  Kullanıcı statu bilgisi sisteme ilk kayıt olan kullanıcılar pasif statusunde kayıt edilir.
    DELETED = 0
    ACTIVE = 1
    PASSIVE = 2
    STATUS_CHOICES = (
        (DELETED, 'DELETED'),
        (ACTIVE, 'ACTIVE'),
        (PASSIVE, 'PASSIVE'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)




