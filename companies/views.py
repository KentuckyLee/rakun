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
        print('...............companies/views/index function called.')
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
        print('...............companies/views/register function called.')
        # REGISTER
        # Register form kontrolü
        form_register = RegisterForm(request.POST or None)
        form_login = LoginForm
        # form valid is
        if form_register.is_valid():
            data_register = form_register.cleaned_data
            company = CompaniesService().find_by_mail_and_phone_number(data_register)
            # Kayıtlı anaokulu olması durumu
            if company is None:
                new_company = CompaniesService().save_company(data_register)
                data_register['company_id'] = new_company.meta.id
                data_register['id'] = new_company.meta.id
                data_register['category_id'] = 1
                new_user = UsersService().save_user(data_register)
                if new_user:
                    messages.success(request, 'Sisteme kaydınız başarılı bir şekilde oluşturulmuştur. '
                                              'Mail adresinize hesap bilgileri iletilmiştir.')
                    return redirect('companies:index')
                else:
                    messages.warning(request, 'Teknik bir hata oluştu!. Kullanıcı kayıt edilmedi.')
            else:
                messages.warning(request, 'Sisteme kayıtlı anaokulu mevcut.')
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
        print('...............companies/views/login function called.')
        form_register = RegisterForm
        form_login = LoginForm(request.POST or None)  # Login form kontrolü
        if form_login.is_valid():  # form valid ise
            data_login = form_login.cleaned_data
            get_user = UsersService().login(data_login)
            print('get_user: ', get_user)
            if get_user is not None:
                for user in get_user:
                    user
                print('user login view:', user)
                if user.status_id == __STATUS_PASSIVE:
                    messages.info(request, 'Yeni şifrenizi oluşturabilirsiniz.')
                    response = redirect('companies:set_new_password')
                    response.set_cookie('company_id', user.company_id)
                    return response
                elif user.status_id == __STATUS_ACTIVE:
                    user_info = {
                        'user_id': user.meta.id,
                        'phone_number': user.phone_number,
                        'company': user.company,
                        'company_id': user.company_id,
                        'user_name': user.user_name,
                        'user_surname': user.user_surname,
                        'mail': user.mail,
                        'category_id': user.category_id,
                        'all_data': user
                    }
                    if user.category_id == 2:
                        user_info['personnel_type'] = user.personnel_type
                    else:
                        user_info['personnel_type'] = 0
                    response = redirect('dashboard:index')
                    response.set_cookie('company_id', user.company_id)
                    Authantication.getInstance().setUser(user_info)
                    return response
                else:
                    messages.info(request, 'Kullanıcı silinmiş.')
            else:
                messages.info(request, 'Sistemde böyle bir kullanıcı bulunamadı.')
                return redirect('companies:index')
        context = {
            'form_register': form_register,
            'form_login': form_login
        }
        return render(request, 'rakun/loginorregister.html', context)
    except Exception as e:
        print(e)


def set_new_password(request):
    try:
        print('...............companies/view/set_new_password function called.')
        if request.COOKIES.get('company_id') is not None:
            new_password_form = NewPasswordForm(request.POST or None)
            if new_password_form.is_valid():  # form valid ise
                data_new_password = new_password_form.cleaned_data
                data_new_password['company_id'] = request.COOKIES.get('company_id')
                update_user = UsersService()
                update_user.user_password_update(data_new_password)
                if update_user:
                    messages.success(request,
                                     'Şifre değiştirme işlemi başarılı. '
                                     'Belirlediğiniz şifre ile sisteme giriş yapabilirsiniz.')
                    return redirect('companies:login')
                else:
                    messages.warning(request, 'Teknik bir hata oluştu. Şifre güncellenmedi.')
                    return redirect('companies:set_new_password')
            context = {
                'new_password_form': new_password_form
            }
            return render(request, 'rakun/newpassword.html', context)
        else:
            raise Exception('sayfayı görüntüleme yetkiniz yok')
    except Exception as e:
        print(e)


def logout(request):
    try:
        print('...............companies/view/logout function called.')
        response = redirect('companies:login')
        response.delete_cookie('company_id')
        Authantication.getInstance().logutInstance()
        return response
    except Exception as e:
        print(e)
