from django.db import models

# Create your models here.

class Students(models.Model):
    student_name = models.CharField(max_length=50, null=False)  # Kullanıcı İsmi
    student_surname = models.CharField(max_length=50, null=False)  # Kullanıcı İsmi
    parent = models.CharField(max_length=50)
    parent_id = models.CharField(null=False, max_length=50)
    class_id = models.CharField(max_length=250)
    class_name = models.CharField(max_length=50)
    image_url = models.FileField(blank=True, null=True)  # Kullanıcı profil resmi
    student_birth_date = models.DateTimeField(auto_now_add=False, null=False)  # Kullanıcının doğu tarihi
    company_id = models.CharField(max_length=40)  # owner kulanıcının telefon numarası
    company = models.CharField(max_length=50)  # Anaokulu ismi
    private_student = models.BooleanField(null=False)
    student_height = models.IntegerField(null=True)
    student_weight = models.IntegerField(null=True)
    student_note = models.TextField(null=True)
    status_id = models.IntegerField(default=2)  # Kullanıcı statusu
    created_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Kayıt tarih
    update_date = models.DateTimeField(auto_now_add=False, blank=True)  # Kullanıcı Güncelleme tarihi
