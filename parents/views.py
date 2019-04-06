from django.shortcuts import render, redirect
from parents.forms import NewParentForm
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
        context = Authantication.getInstance().getUser()
        context['page'] = 'Veliler'
        all_parent = ParentService().get_all_parent(context)
        context['page_data'] = all_parent
        return render(request, 'rakun/parents/parent_list.html', context)
    except Exception as e:
        print(e)


def set_new_parent(request):
    try:
        print('...............parents/view/set_new_parent function called.')
        context = Authantication.getInstance().getUser()
        parent_form = NewParentForm(data=request.POST or None)
        student_form = NewStudentForm(data=request.POST or None, request=request.COOKIES.get('company_id'))
        context['parent_form'] = parent_form
        context['student_form'] = student_form
        if parent_form.is_valid() and student_form.is_valid():
            data_parent = parent_form.cleaned_data
            data_parent['company_id'] = request.COOKIES.get('company_id')
            data_parent['company'] = context['company']
            data_parent['category_id'] = 3
            data_student = student_form.cleaned_data
            query_active_parent = ParentService().get_parent(d=data_parent)
            # sistemde kayıtlı parent var
            if query_active_parent is not None:
                messages.warning(request, 'Veli daha önce sistemde kayıtlı.')
                return redirect('parents:set_new_parent')
            else:
                # yeni parent
                parent_save = ParentService().save_parent(data_parent)
                #parent kaydı başarılı
                if parent_save:
                    time.sleep(1)
                    get_parent = ParentService().get_parent(data_parent)
                    print('get_parent: ', get_parent)
                    user_save = UsersService().save_user(data_parent)
                    # user kaydı başarılı
                    if user_save:
                        for parent in get_parent:
                            # paren id ve name alınıyor
                            data_student['parent_id'] = parent.meta.id
                            data_student['parent'] = parent.user_name + ' ' + parent.user_surname
                        data_student['company_id'] = request.COOKIES.get('company_id')
                        data_student['company'] = context['company']
                        d = {'_id': data_student['class_room']}
                        # formdan alınana class çağrılı
                        get_class = ClassService().get_class(d)
                        if get_class is not None:
                            for data in get_class:
                                registered_student = data.registered_student
                                data_student['class_name'] = data.class_name
                            registered_student += data_parent['students_count']
                            d['registered_student'] = registered_student
                            student_save = StudentService().save_student(data_student)
                            if student_save:
                                ClassService().registered_student_update(d)
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
        context = Authantication.getInstance().getUser()
        results = ParentService().get_parent({'id': id, 'company_id': request.COOKIES.get('company_id')})
        for profile in results:
            profile
        students = StudentService().get_student({'parent_id': profile.meta.id, 'company_id': request.COOKIES.get('company_id')})
        context['page'] = 'Veli / ' + profile.user_name + ' ' + profile.user_surname
        context['profile'] = profile
        context['page_data'] = students
        return render(request, 'rakun/parents/parent_content.html', context)

    except Exception as e:
        print(e)

