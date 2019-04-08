from django.shortcuts import render, redirect
from parents.forms import NewParentForm, EditParentFrom
from users.forms import UserAccountSetting
from students.forms import NewStudentForm
from Context.ContextView import Authantication
from parents.service import ParentService
from students.service import StudentService
from users.services import UsersService
from django.contrib import messages
from classes.service import ClassService
import time

# Create your views here.


def index(request):
    try:
        print('...............parents/view/index function called.')
        # Login kullanıcı bilgisi
        context = Authantication.getInstance().getUser()
        # Company e ait statusu 1 olan velilerin listesi
        all_parent = ParentService().get_all_parent(context)
        context['page'] = 'Veliler'
        context['page_data'] = all_parent
        return render(request, 'rakun/parents/parent_list.html', context)
    except Exception as e:
        print(e)


def set_new_parent(request):
    try:
        print('...............parents/view/set_new_parent function called.')
        # Login kullanıcı bilgisi
        context = Authantication.getInstance().getUser()
        # Veli ve öğrenci formu alınır context ile ekrana gönderilir.
        parent_form = NewParentForm(data=request.POST or None)
        student_form = NewStudentForm(data=request.POST or None, request=request.COOKIES.get('company_id'))
        context['parent_form'] = parent_form
        context['student_form'] = student_form
        # Form lar valid True
        if parent_form.is_valid() and student_form.is_valid():
            # Veli datası alınır ve hazırlanır
            data_parent = parent_form.cleaned_data
            data_parent['company_id'] = request.COOKIES.get('company_id')
            data_parent['company'] = context['company']
            data_parent['category_id'] = 3
            # Öğrenci datası alınır ve hazırlanır
            data_student = student_form.cleaned_data
            query_active_parent = ParentService().find_by_phone_number_and_company_id(data_parent)
            query_active_user = UsersService().get_user(data_parent)
            # sisteme kayıtlı parent ve user kaydı var!
            if query_active_parent is not None and query_active_user is not None:
                messages.warning(request, 'Veli daha önce sistemde kayıtlı.')
            # Kayıt yapılabilir durum
            else:
                # Parent Kaydı yapılır
                parent_save = ParentService().save_parent(data_parent)
                # Parent kaydının başarılı olduğu durum
                if parent_save:
                    time.sleep(1)
                    parent_id = parent_save.meta.id
                    get_parent = ParentService().find_by_id({'id': parent_id})
                    # User Kaydı yapılır
                    data_parent['id'] = parent_id
                    user_save = UsersService().save_user(data_parent)
                    # user kaydı başarılı
                    if user_save:
                        for parent in get_parent:
                            # parent id ve name alınıyor. Öğrenci datası hazırlanır
                            data_student['parent_id'] = parent_id
                            data_student['parent'] = parent.user_name + ' ' + parent.user_surname
                        data_student['company_id'] = request.COOKIES.get('company_id')
                        data_student['company'] = context['company']
                        # formdan alınana class çağrılır
                        d = {'id': data_student['class_room']}
                        get_class = ClassService().find_by_id(d)
                        # Class room' a Kayıtlı öğrenci sayısında artırılır
                        if get_class is not None:
                            for data in get_class:
                                registered_student = data.registered_student
                                data_student['class_name'] = data.class_name
                            registered_student += data_parent['students_count']
                            d['registered_student'] = registered_student
                            # Öğrenci kaydı yapılır
                            student_save = StudentService().save_student(data_student)
                            if student_save:
                                # Sınıf update edilir.
                                ClassService().update(d)
                            else:
                                raise Exception('error while class updating')
                        else:
                            raise Exception('error class is null')
                    else:
                        raise Exception('error while user registering')
                else:
                    messages.warning(request, 'Teknik bir hata oluştu')
                messages.success(request, 'Veli ve öğrenci kaydı başarıyla oluşturuldu.')
                return redirect('parents:set_new_parent')
        return render(request, 'rakun/parents/set_new_parent.html', context)
    except Exception as e:
        print(e)

def get_profile(request, id):
    try:
        print('...............parents/view/get_profile function called.')
        # Login kullanıcı bilgileri
        context = Authantication.getInstance().getUser()
        # Profile gelen personelin user ve personel tablosundaki bilgileri alınır
        results_parent = ParentService().find_by_id({'id': id})
        results_user = UsersService().find_by_id({'id': id})
        # Veli bilgileri alınır
        parent_data = results_parent[0]
        # Velinin Çokuklar
        students = StudentService().find_by_parent_id_and_company_id({'parent_id': parent_data.meta.id, 'company_id': request.COOKIES.get('company_id')})
        # Profil ve hesap için formlar oluşturulur
        edit_form_parent = EditParentFrom(data=request.POST or None, initial=results_parent.hits.hits[0]['_source'])
        edit_user_account = UserAccountSetting(data=request.POST or None, initial=results_user.hits.hits[0]['_source'])
        # Sayfaya gönderilecek bilgiler hazırlanır
        context['edit_form_parent'] = edit_form_parent
        context['edit_form_user_account'] = edit_user_account
        context['page'] = 'Veli / ' + parent_data.user_name + ' ' + parent_data.user_surname
        context['profile'] = parent_data
        context['page_data'] = students
        return render(request, 'rakun/parents/parent_content.html', context)
    except Exception as e:
        print(e)

def parent_update(request, parent_id):
    try:
        print('...............parents/view/parent_update function called.')
        # Profil bilgileri update edilme isteği geldi
        update_form = EditParentFrom(data=request.POST)
        # Form valid True
        if update_form.is_valid():
            data = update_form.cleaned_data
            data['id'] = parent_id
            # Veli bilgileri update edilir.
            update_parent = ParentService().update(data)
            if update_parent:
                # User bilgileri update edilir.
                update_user = UsersService().update(data)
                messages.success(request, 'Personel güncellenmiştir.')
            else:
                messages.warning(request, 'Teknik hata! Güncelleme işlmei başarısız oldu.')
        return redirect('parents:index')
    except Exception as e:
        print(e)

def account_update(request, parent_id):
    try:
        print('...............parents/view/account_update function called.')
        # Velinin hesap bilgileri update edilme isteği geldi.
        update_account = UserAccountSetting(data=request.POST)
        # form valid True
        if update_account.is_valid():
            # Form bilgileri alınır
            data = update_account.cleaned_data
            data['id'] = parent_id
            data['company_id'] = request.COOKIES.get('company_id')
            # Personel ve user tablosu update edilir
            update_user = UsersService().user_password_update(data)
            if update_user:
                messages.success(request, 'Hesap bilgileri güncellenmiştir.')
            else:
                messages.warning(request, 'Teknik hata! Güncelleme işlmei başarısız oldu.')
        return redirect('parents:index')
    except Exception as e:
        print(e)
