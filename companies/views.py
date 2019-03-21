from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from elasticsearch import Elasticsearch
from datetime import datetime
from companies.forms import RegisterForm, LoginForm, NewPasswordForm
from companies.services import CompaniesService
from users.services import UsersService
import hashlib


#  Create your views here.


def index(request):
    try:
        form_register = RegisterForm
        form_login = LoginForm
        context = {
            'form_login': form_login,
            'form_register': form_register
        }
        return render(request, 'rakun/loginorregister.html', context)
    except Exception as e:
            print(e)

def register(request):

    try:
        # REGISTER
        # Register form kontrolü
        form_register = RegisterForm(request.POST or None)
        form_login = LoginForm
        # form valid is
        if form_register.is_valid():
            data_register = form_register.cleaned_data
            new_company = CompaniesService()
            # Sistemde kayıtlı aktif anaokulu sayısı
            query = CompaniesService().get_active_companies_count(data_register)
            # Kayıtlı anaokulu olması durumu
            if query.hits.total != 0:
                messages.warning(request, 'Uyarı! Sistemde daha önce kaydınız bulunmaktadır.')
            # Aktif anaokulu kaydı bulunmadığı durum
            else:
                # Yeni anaokulu kaydı yapılır
                company = new_company.save_company(data_register)
                if company.meta.id:
                    # Owner datası hazırlanır
                    data_register['company_id'] = company.meta.id
                    data_register['category_id'] = 1  # OWNER kategorisi (1)
                    new_user = UsersService()
                    # Owner kullanıcısı users tablosuna kayıt edilir ve mail atılır
                    new_user.save_user(data_register)
                    messages.success(request, 'Sisteme kaydınız başarılı bir şekilde oluşturulmuştur. Mail adresinize hesap bilgileri iletilmiştir.')
                # Anaokulu kayıt edilemedi
                else:
                    messages.warning(request, 'Teknik bir hata oluştu!')
        # form valid değil
        else:
            messages.warning(request, 'Girilen telefon numaraları uyuşmamaktadır.')
        context = {
            'form_register': form_register,
            'form_login': form_login
        }
        return render(request, 'rakun/loginorregister.html', context)
    except Exception as e:
        print(e)


    # form = RegisterForm(request.POST or None)
    #
    # if form.is_valid():
    #     data = form.cleaned_data
    #     context = {
    #         'data': data,
    #         'form': form
    #     }
    #     return render(request, 'rakun/test.html', context)
    #
    # context = {
    #     'form': form
    # }
    # return     # if request.method != 'POST':  # Post işlemi başarılı durumu
    #     messages.warning(request, 'Teknik bir hata oluştu.')
    #     return render(request, 'rakun/loginorregister.html')
    #
    # else:  # Post işlemi başarılı durumu
    #     phone_number = request.POST.get('phone_number')
    #     phone_replace = request.POST.get('phone_replace')
    #     company = request.POST.get('company')
    #     owner_name = request.POST.get('owner_name')
    #     owner_surname = request.POST.get('owner_surname')
    #     mail = request.POST.get('mail')
    #     credit = 3
    #     credits_price = 0
    #     credits_price_date = datetime.now()
    #     credits_expiration_date = datetime.now() + relativedelta(months=+1)
    #     created_date = datetime.now()
    #     update_date = datetime.now()
    #     password = BaseUserManager().make_random_password(6)
    #
    #
    #     if phone_number != phone_replace:  # Telefon numaralarının eşit olmadığı durum
    #         messages.warning(request, 'Girdiğiniz telefon numaraları eşleşmemektedir.')
    #         return render(request, 'rakun/loginorregister.html')
    #
    #     else:  # Telefon numaraların eşit olduğu durum
    #         # Telefon numarası ve mail adresi bulunan aktif kullanıcı
    #         result = TestCompaniesDocument.search().query(
    #             Q('match_phrase', mail=mail) |
    #             Q('match_phrase', phone_number=phone_number) &
    #             Q('match_phrase', status=1)
    #         )
    #         response = result.execute()
    #         if response.hits.total != 0:  # Sisteme daha önceden kayıt yapldığı durum
    #             messages.warning(request, 'Uyarı! Sistemde daha önce kaydınız bulunmaktadır.')
    #             return render(request, 'rakun/loginorregister.html')
    #
    #         else:  # Sisteme yeni anaokul kaydı yapılacak
    #             # Yeni anaokulu bilgisi oluşturulur
    #             new_company = TestCompaniesDocument(
    #                 phone_number=phone_number,
    #                 company_id=phone_number,
    #                 company=company,
    #                 owner_name=owner_name,
    #                 owner_surname=owner_surname,
    #                 mail=mail,
    #                 credit=credit,
    #                 credits_price=credits_price,
    #                 credits_price_date=credits_price_date,
    #                 credits_expiration_date=credits_expiration_date,
    #                 country='undefined',
    #                 city='undefined',
    #                 district='undefined',
    #                 created_date=created_date,
    #                 update_date=update_date,
    #                 status=2
    #             )
    #             new_company.save()  # Ana Okulu kaydı Yapılır
    #             # Yeni superUser bilgisi oluşturulur
    #             new_user = TestPersonnelDocument(
    #                 # Personnel data
    #                 user_name=owner_name,
    #                 user_surname=owner_surname,
    #                 mail=mail,
    #                 image_url='undefined',
    #                 birth_date=created_date,
    #                 address='undefined',
    #                 university='undefined',
    #                 domain='undefined',
    #                 language='undefined',
    #                 graduated_date=created_date,
    #                 # Personnel authenticate data
    #                 phone_number=phone_number,
    #                 password=password,
    #                 company_id=phone_number,
    #                 company=company,
    #                 class_room=0,
    #                 position=1,  # owner
    #                 category=1,  # owner
    #                 status=2,  # passive
    #                 created_date=created_date,
    #                 update_date=update_date,
    #
    #             )
    #             new_user.save()  # Yeni superUser kaydı yapılır
    #
    #             if HttpResponse.status_code != 200:  # Kayıt işlemi başarısız
    #                 messages.warning(request, 'Teknik bir hata oluştu.')
    #                 return render(request, 'rakun/loginorregister.html')
    #
    #             else:  # Kayıt işlemi başarılı
    #                 # Kullanıcının telefon numarası otomatik password gönderilecek
    #                 messages.success(request,
    #                                  'Kayıt işlemi yapılmıştır. Telefonuza gönderilen şifreniz ile sisteme giriş yapabilirsiniz')
    #                 context = {'password': password}
    #                 return render(request, 'rakun/loginorregister.html', context)


def login(request):
    try:
        form_register = RegisterForm
        form_login = LoginForm(request.POST or None)  # Login form kontrolü
        if form_login.is_valid():  # form valid ise
            data_login = form_login.cleaned_data
            user = UsersService()
            status = user.get_user_status(data_login)
            if status[0] == 2:
                messages.info(request, 'Yeni şifrenizi oluşturabilirsiniz.')
                response = redirect('companies:set_new_password')
                response.set_cookie('company_id', status[2])
                return response
            elif status[0] == 1:
                response = redirect('dashboard:index')
                response.set_cookie('company_id', status[2])
                return response
        context = {
            'form_register': form_register,
            'form_login': form_login
        }
        return render(request, 'rakun/loginorregister.html', context)
    except Exception as e:
        print(e)
    # return render(request, 'rakun/test.html')
    # if request.method != 'POST':  # Post işlemi başarısız
    #     messages.warning(request, 'Teknik bir hata oluştu')
    #     return render(request, 'rakun/loginorregister.html')
    #
    # else:  # Post işlemi başarılı
    #     phone_number = request.POST.get('login_phone')
    #     password = request.POST.get('login_password')
    #     # Telefon numarası ve password ile eşleşen kayıtlar
    #     query = TestPersonnelDocument.search().query(
    #         Q('match_phrase', phone_number=phone_number) &
    #         Q('match_phrase', password=password) |
    #         Q('match_phrase', password=hashlib.md5(password.encode('utf8')).hexdigest())
    #     )
    #     query_results = query.execute()
    #     # Eşleşen kayıtların statu bilgisi alınır
    #     result_status = 0
    #     for query_result in query_results:
    #         if query_result.status == 1:
    #             status = 1
    #         elif query_result.status == 2:
    #             status = 2
    #         else:
    #             status = 3
    #     if status == 3:  # Sistemde kullanıcı silinmiş
    #         messages.info(request, 'Girdiğiniz bilgiler ile eşleşen bir kullanıcı bulunmamktadır')
    #         return render(request, 'rakun/loginorregister.html')
    #     elif status == 2:  # Pasif statudeki kullanıcı.
    #         return render(request, 'rakun/newpassword.html')
    #     elif status == 1:  # Aktif kullanıcı.
    #         doc_id = query_results.hits.hits[0]['_id']
    #         response = redirect('dashboard:index')
    #         response.set_cookie('doc_id', doc_id)
    #         return response
    #     else:  # Sistemde kullanıcı bulunmuyor
    #         messages.info(request, 'Girdiğiniz bilgiler ile eşleşen bir kullanıcı bulunmamktadır')
    #         return render(request, 'rakun/loginorregister.html')


def set_new_password(request):
    new_password_form = NewPasswordForm(request.POST or None)
    if new_password_form.is_valid():  # form valid ise
        data_new_password = new_password_form.cleaned_data
        data_new_password['company_id'] = request.COOKIES.get('company_id')
        update_user = UsersService()
        if update_user.user_password_update(data_new_password) != 0:
            messages.success(request, 'Şifre değiştirme işlemi başarılı. Belirlediğiniz şifre ile sisteme giriş yapabilirsiniz.')
            return redirect('companies:login')
        else:
            messages.warning(request, 'Teknik bir hata oluştu.')
    context = {
        'new_password_form': new_password_form
    }
    return render(request, 'rakun/newpassword.html', context)



    # if request.method != 'POST':  # POST işlemi başarısız
    #     messages.warning(request, 'Teknik bir hata oluştu.')
    #     return render(request, 'rakun/newpassword.html')
    #
    # else:  # POST işlemi başarılı
    #     password = request.POST.get('password')
    #     password_replace = request.POST.get('password_replace')
    #     phone_number = request.POST.get('login_phone')
    #     update_date = datetime.now()
    #
    #     if password != password_replace:  # Passwordlerin eşleşmediği durum
    #         messages.warning(request, 'Girilen şifreler eşleşmemektedir.')
    #         return render(request, 'rakun/newpassword.html')
    #
    #     else:  # Passwordlerin eşleştiği durum
    #         password = hashlib.md5(password.encode('utf8')).hexdigest()
    #         client = Elasticsearch()
    #         response = client.update_by_query(
    #             index="test_personnel",
    #             body={
    #                 "query": {
    #                     "bool": {
    #                         "must": [
    #                             {"match": {"phone_number": phone_number}},
    #                             {"match": {"status": 2}}
    #                         ]
    #                     }
    #                 },
    #                 "script": {
    #                     "inline": "ctx._source[params.field0] = params.value0;"
    #                               "ctx._source[params.field1] = params.value1;"
    #                               "ctx._source[params.field2] = params.value2;",
    #                     "params": {
    #                         "field0": "password",
    #                         "value0": password,
    #                         "field1": "status",
    #                         "value1": 1,
    #                         "field2": "update_date",
    #                         "value2": update_date,
    #                     },
    #                 }
    #             },
    #         )
    #         if HttpResponse.status_code != 200:  # Kayıt işlemi başarısız
    #             messages.warning(request, 'Güncelleme işlemi başarısız oldu.')
    #             return render(request, 'rakun/loginorregister.html')
    #
    #         else:  # Kayıt işlemi başarılı
    #             # Kullanıcının telefon numarası otomatik password gönderilecek
    #             messages.success(request, 'Şifreniz güncellenmiştir. Sisteme giriş yapabilirsiniz.')
    #             context = {'password': password, 'sonuc': response}
    #             return render(request, 'rakun/loginorregister.html', context)
