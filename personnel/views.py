from django.shortcuts import render, redirect
from Context.ContextView import Authantication
from personnel.services import PersonnelService
from students.service import StudentService
from personnel.forms import NewPersonnelForm
from users.services import UsersService
from django.contrib import messages
from notifications.service import NotificationService
import time


def index(request):
    try:
        print('.................personnels/views/index function called')
        context = Authantication.getInstance().getUser()
        context['page'] = 'Personel'
        all_personnel = PersonnelService().get_all_personnels({'company_id': request.COOKIES.get('company_id')})
        context['page_data'] = all_personnel
        return render(request, 'rakun/personnel/personnel_list.html', context)
    except Exception as e:
        print(e)


def set_new_personnel(request):
    try:
        print('.................personnels/views/set_new_personnel function called')
        context = Authantication.getInstance().getUser()
        personnel_form = NewPersonnelForm(data=request.POST or None, request=request.COOKIES.get('company_id'))
        context['form'] = personnel_form
        if personnel_form.is_valid():
            data_personnel = personnel_form.cleaned_data
            data_personnel['company_id'] = request.COOKIES.get('company_id')
            data_personnel['company'] = context['company']
            print('data Personel: ', data_personnel)
            query_active_personnel = PersonnelService().get_personnel(data_personnel)
            query_active_user = UsersService().get_user(data_personnel)
            print('user personel: ', query_active_user)
            if query_active_personnel is not None or query_active_user is not None:
                messages.info(request, 'Sisteme kayıtlı böyle bir personel bulunmaktadır.')
            else:
                new_personnel = PersonnelService().save_personnel(data_personnel)
                new_user = UsersService().save_user(data_personnel)
                if new_personnel and new_user:
                    time.sleep(1)
                    get_all_personnel = PersonnelService().get_all_personnels(data_personnel)
                    personnel_id = list()
                    for data in get_all_personnel:
                        personnel_id.append(data.meta.id)
                    d = {
                        'created_user_id': context['user_id'],
                        'assigned_user_id': personnel_id,
                        'company_id': request.COOKIES.get('company_id'),
                        'content': '{} {}, {} ailesine katıldı. Ona "merhaba" de!'.format(data_personnel['user_name'], data_personnel['user_surname'], data_personnel['company'])
                    }
                    NotificationService().save_notification(d)
                    messages.success(request, 'Personel kaydı başarıyla oluşturuldu.')
                    return redirect('personnel:set_new_personnel')
                else:
                    messages.warning(request, 'Kayıt işleminde hata oluştu.')
        return render(request, 'rakun/personnel/set_new_personnel.html', context)
    except Exception as e:
        print(e)

def get_profile(request, id):
    try:
        context = Authantication.getInstance().getUser()
        profile_query = {
            'id': id,
            'company_id': request.COOKIES.get('company_id')
        }
        results = PersonnelService().get_personnel(profile_query)
        for profile in results:
            profile
        print('class: ', profile.class_room, profile)
        students = StudentService().personnel_students({'class_room': profile.class_room, 'company_id':request.COOKIES.get('company_id')})
        personnel_students = list()
        for student in students:
            for data_student in student:
                personnel_students.append(data_student)
        print('students: ', data_student)
        context['page'] = 'Personel / ' + profile.user_name + ' ' + profile.user_surname
        context['profile'] = profile
        context['page_data'] = personnel_students
        return render(request, 'rakun/personnel/personnel_content.html', context)
    except Exception as e:
        print(e)

def personnel_update(request, id):
    pass

def personnel_delete(requst, id):
    pass


