from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.base_user import BaseUserManager
from loginorregister.document import TestDocument
from elasticsearch_dsl.query import Q
from datetime import datetime
from dateutil.relativedelta import *

#  Create your views here.


def index(request):
    return render(request, 'rakun/loginorregister.html')


def register(request):
    if request.method != 'POST':  # Post işlemi başarılı durumu
        messages.info(request, 'Teknik bir hata oluştu.')
        return render(request, 'rakun/test.html')

    else:  # Post işlemi başarılı durumu
        phone_number = request.POST.get('phone_number')
        phone_replace = request.POST.get('phone_replace')
        mail = request.POST.get('mail')
        company = request.POST.get('company')
        owner_name = request.POST.get('owner_name')
        password = BaseUserManager().make_random_password(6)
        credits_price = 0
        credits_price_date = datetime.now()
        credits_expiration_date = datetime.now() + relativedelta(months=+1)
        created_date = datetime.now()
        status = 2
        credit = 3
        image_url = 'default'
        country = 'default'
        city = 'default'
        district = 'default'

        if phone_number != phone_replace:  # Telefon numaralarının eşit olmadığı durum
            messages.warning(request, 'Girdiğiniz telefon numaraları eşleşmemektedir.')
            return render(request, 'rakun/loginorregister.html')

        else:  # Telefon numaraların eşit olduğu durum
            # Telefon numarası ve mail adresi bulunan aktif kullanıcı
            result = TestDocument.search().query(
                Q('match_phrase', mail=mail) &
                Q('match_phrase', phone_number=phone_number) &
                Q('match_phrase', status=2)
            )
            response = result.execute()
            if response.hits.total > 0:  # Sisteme daha önceden kayıt yapldığı durum
                messages.warning(request, 'Uyarı! Sistemde daha önce kaydınız bulunmaktadır.')
                return render(request, 'rakun/loginorregister.html')

            else:  # Sisteme yeni anaokul kaydı yapılacak
                # Yeni anaokulu ve Kullanıcı bilgisi Eklenir
                new_company = TestDocument(
                    phone_number=phone_number,
                    company=company,
                    password=password,
                    owner=owner_name,
                    mail=mail,
                    credit=credit,
                    credits_price=credits_price,
                    credits_price_date=credits_price_date,
                    credits_expiration_date=credits_expiration_date,
                    image_url=image_url,
                    country=country,
                    city=city,
                    district=district,
                    created_date=created_date,
                    status=status
                )
                new_company.save()  # Kullanıcı kayıt edilir

                if HttpResponse.status_code != 200:  # Kayıt işlemi başarısız
                    messages.warning(request, 'Teknik bir hata oluştu.')
                    return render(request, 'rakun/loginorregister.html')

                else:  # Kayıt işlemi başarılı
                    # Kullanıcının telefon numarası otomatik password gönderilecek
                    messages.success(request, 'Kayıt işlemi yapılmıştır. Telefonuza gönderilen şifreniz ile sisteme giriş yapabilirsiniz')
                    return render(request, 'rakun/loginorregister.html')


def login(request):
    pass





