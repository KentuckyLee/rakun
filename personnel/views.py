from django.shortcuts import render, redirect
from Context.ContextView import Authantication
from personnel.services import PersonnelService
from students.service import StudentService
from personnel.forms import NewPersonnelForm, EditPersonnel
from users.forms import UserAccountSetting
from users.services import UsersService
from django.contrib import messages
import time


def index(request):
    try:
        print('.................personnels/views/index function called')
        # Login Kullanıcı bilgileri
        context = Authantication.getInstance().getUser()
        # Company e ait statusu 1 olan tüm personeller
        all_personnel = PersonnelService().get_all_personnels({'company_id': request.COOKIES.get('company_id')})
        # Personeller ve Login olan kullanıc bilgisi context ile sayfaya iletiliyor.
        context['page_data'] = all_personnel
        context['page'] = 'Personel'
        return render(request, 'rakun/personnel/personnel_list.html', context)
    except Exception as e:
        print(e)


def set_new_personnel(request):
    try:
        print('.................personnels/views/set_new_personnel function called')
        # Login kullanıcı bilgileri
        context = Authantication.getInstance().getUser()
        # Personel formu alınır
        personnel_form = NewPersonnelForm(data=request.POST or None, request=request.COOKIES.get('company_id'))
        # Oluşturulan form context ile sayfaya gönderilir
        context['form'] = personnel_form
        # Formdan gelen data valid sorgusu TRUE
        if personnel_form.is_valid():
            # Formdan gelen datalar değişkene aktarılır
            data_personnel = personnel_form.cleaned_data
            # Gelen dataya company ve cookie deki company_id değeri setlenir.
            data_personnel['company_id'] = request.COOKIES.get('company_id')
            data_personnel['company'] = context['company']
            # Personel kaydı yapılmadan önce aktif personel ve user var mı kontrol edilir.
            query_active_personnel = PersonnelService().find_by_phone_number_and_company_id(data_personnel)
            query_active_user = UsersService().get_user(data_personnel)
            # Aktif personel yada kullanıcı olduğu durum. Kayıt yapılmaz
            if query_active_personnel is not None or query_active_user is not None:
                messages.info(request, 'Sisteme kayıtlı böyle bir personel bulunmaktadır.')
            # Kayıt yapılabilir durum
            else:
                # Personel kaydı yapılır
                new_personnel = PersonnelService().save_personnel(data_personnel)
                # Personel kaydının başarılı olduğu durum
                if new_personnel:
                    time.sleep(1)
                    # Kayıt edilen personelin document id değeri alınır ve yeni user kayıt edilir
                    data_personnel['id'] = new_personnel.meta.id
                    new_user = UsersService().save_user(data_personnel)
                    if new_user:
                        messages.success(request, 'Personel kaydı başarıyla oluşturuldu.')
                        return redirect('personnel:set_new_personnel')
                    else:
                        raise Exception('error while user registering')
                else:
                    messages.warning(request, 'Personel kaydı yapılırken hata ile karşılaşıldı.')
        return render(request, 'rakun/personnel/set_new_personnel.html', context)
    except Exception as e:
        print(e)

def get_profile(request, pers_id):
    try:
        # Login kullanıcı bilgileri
        context = Authantication.getInstance().getUser()
        # Profile gelen personelin user ve personel tablosundaki bilgileri alınır
        results_personnel = PersonnelService().find_by_id({'id': pers_id})
        results_user = UsersService().find_by_id({'id': pers_id})
        # Profil ve Hesap bilgileri formları oluşturulur
        edit_form_personnel = EditPersonnel(data=request.POST or None, request={'company_id': request.COOKIES.get('company_id')}, initial=results_personnel.hits.hits[0]['_source'])
        edit_user_account = UserAccountSetting(data=request.POST or None, initial=results_user.hits.hits[0]['_source'])
        # Personelin bilgileri alınır
        personnel_data = results_personnel[0]
        # Personel öğretmen ise ilişkili olduğu öğrencilerin listesi oluşturulur ve context ile gönderilir.
        print('personnel_data.personnel_type:  ', personnel_data.personnel_type)
        if personnel_data.personnel_type == 1:
            related_students = StudentService().personnel_students({'class_room': personnel_data.class_room, 'company_id':request.COOKIES.get('company_id')})
            personnel_students = list()
            for students in related_students:
                for student in students:
                    personnel_students.append(student)
            context['page_data'] = personnel_students
        # Formlar ve dier profil bilgileri gönderilir.
        context['edit_form_personnel'] = edit_form_personnel
        context['edit_form_user_account'] = edit_user_account
        context['page'] = 'Personel / ' + personnel_data.user_name + ' ' + personnel_data.user_surname
        context['profile'] = personnel_data
        return render(request, 'rakun/personnel/personnel_content.html', context)
    except Exception as e:
        print(e)


def personnel_update(request, pers_id):
    try:
        # Profil bilgileri update edilme isteği geldi
        update_form = EditPersonnel(data=request.POST, request={'company_id': request.COOKIES.get('company_id')})
        # form valid True
        if update_form.is_valid():
            # Formdan gelen bilgiler alınır
            data = update_form.cleaned_data
            data['id'] = pers_id
            # Personelin profil bilgileri update edilir.
            update_personnel = PersonnelService().update(data)
            if update_personnel:
                # Personelin user bilgileri update edilir.
                UsersService().update(data)
                messages.success(request, 'Personel güncellenmiştir.')
            else:
                messages.warning(request, 'Teknik hata! Güncelleme işlmei başarısız oldu.')
        return redirect('personnel:index')
    except Exception as e:
        print(e)

def account_update(request, pers_id):
    try:
        # Personelin hesap bilgileri update edilme isteği geldi.
        update_account = UserAccountSetting(data=request.POST)
        # form valid True
        if update_account.is_valid():
            # Form bilgileri alınır
            data = update_account.cleaned_data
            data['id'] = pers_id
            data['company_id'] = request.COOKIES.get('company_id')
            # Personel ve user tablosu update edilir
            update_user = UsersService().user_password_update(data)
            if update_user:
                messages.success(request, 'Hesap bilgileri güncellenmiştir.')
            else:
                messages.warning(request, 'Teknik hata! Güncelleme işlmei başarısız oldu.')
        return redirect('personnel:index')
    except Exception as e:
        print(e)


def personnel_delete(requst, id):
    pass


