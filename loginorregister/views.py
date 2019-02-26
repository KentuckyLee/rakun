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

    if request.method == 'POST':  # Post işlemi başarılı durumu

        phone_number = request.POST.get('phone_number')
        phone_replace = request.POST.get('phone_replace')
        mail = request.POST.get('mail')
        company = request.POST.get('company')
        owner_name = request.POST.get('owner_name')
        password = BaseUserManager().make_random_password(6)
        credits_price = 0
        credits_price_date = datetime.now()
        credits_expiration_date = datetime.now()+relativedelta(months=+1)
        created_date = datetime.now()
        status = 2
        credit = 3
        image_url = 'default'
        country = 'default'
        city = 'default'
        district = 'default'

        newCompany = TestDocument(
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
        newCompany.save()

        context = {
            'status' : status,
            'phone_number' : phone_number,
            'phone_replace' : phone_replace,
            'mail' : mail,
            'company': company,
            'owner_name' : owner_name,
            'password' : password,
            'credit': credit,
            'credits_price': credits_price,
            'credits_price_date' : credits_price_date,
            'credits_expiration_date' : credits_expiration_date,
            'created_date': created_date,
            'image_url': image_url,
            'country': country,
            'city': city,
            'district': district,


        }
        messages.info(request, 'Post İşlemi Başarılı  Kayıtlar Başarıyla Oluşturuldu.')
        return render(request, 'rakun/test.html', context)

    else:  # POST işlemi başarısız olduğu durum

        messages.info(request, 'POST İşlemi Başarısız.')
        return render(request, 'rakun/test.html')


def login(request):
    pass






