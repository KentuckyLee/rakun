from django.contrib import messages
from django.shortcuts import render, redirect
from Context.ContextView import Authantication
from companies.forms import RegisterForm, LoginForm, NewPasswordForm
from companies.services import CompaniesService
from users.services import UsersService

__STATUS_ACTIVE = 1
__STATUS_PASSIVE = 2
__STATUS_DELETE = 3


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
                    messages.success(request,
                                     'Sisteme kaydınız başarılı bir şekilde oluşturulmuştur. Mail adresinize hesap bilgileri iletilmiştir.')
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


def login(request):
    try:
        form_register = RegisterForm
        form_login = LoginForm(request.POST or None)  # Login form kontrolü
        if form_login.is_valid():  # form valid ise
            data_login = form_login.cleaned_data
            user = UsersService()
            data = user.get_user(data_login)
            print('user_name: {} \n user_surname: {} \n company: {} \n phone_number: {} \n password: {}'.format(
                data.user_name, data.user_surname, data.company, data.phone_number, data.password))
            if data.status_id == __STATUS_PASSIVE:
                messages.info(request, 'Yeni şifrenizi oluşturabilirsiniz.')
                response = redirect('companies:set_new_password')
                response.set_cookie('company_id', data.company_id)
                return response
            elif data.status_id == __STATUS_ACTIVE:

                response = redirect('dashboard:index')
                response.set_cookie('company_id', data.company_id)
                user_info = {
                    'phone_number': data.phone_number,
                    'company': data.company,
                    'user_name': data.user_name,
                    'user_surname': data.user_surname,
                    'mail': data.mail
                }
                Authantication.getInstance().setUser(user_info)
                return response
        context = {
            'form_register': form_register,
            'form_login': form_login
        }
        return render(request, 'rakun/loginorregister.html', context)
    except Exception as e:
        print(e)


def set_new_password(request):
    try:
        new_password_form = NewPasswordForm(request.POST or None)
        if new_password_form.is_valid():  # form valid ise
            data_new_password = new_password_form.cleaned_data
            data_new_password['company_id'] = request.COOKIES.get('company_id')
            update_user = UsersService()
            if update_user.user_password_update(data_new_password) != 0:
                messages.success(request,
                                 'Şifre değiştirme işlemi başarılı. Belirlediğiniz şifre ile sisteme giriş yapabilirsiniz.')
                return redirect('companies:login')
            else:
                messages.warning(request, 'Teknik bir hata oluştu.')
        context = {
            'new_password_form': new_password_form
        }
        return render(request, 'rakun/newpassword.html', context)
    except Exception as e:
        print(e)


def logout(request):
    try:
        response = redirect('companies:login')
        response.delete_cookie('company_id')
        Authantication.getInstance().logutInstance()
        return response
    except Exception as e:
        print(e)
