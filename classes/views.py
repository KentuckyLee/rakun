from django.shortcuts import render, redirect
from django.contrib import messages
from Context.ContextView import Authantication
from classes.forms import NewClassFrom
from classes.service import ClassService
from personnel.services import PersonnelService
from students.service import StudentService
from students.forms import StudentInspectionForm


def index(request):
    try:
        print('.................classes/views/index function called')
        context = Authantication.getInstance().getUser()
        context['page'] = 'Sınıflar'
        all_class = ClassService().get_all_class(context)
        personnel_list = list()
        for i in all_class:
            get_pers = PersonnelService().related_class({'class_room': i.meta.id})
            for pers_data in get_pers:
                personnel_list.append((pers_data.user_name + ' ' + pers_data.user_surname, i.meta.id, pers_data.meta.id))
        print('all_class: ', all_class)
        context['page_data'] = all_class
        context['personnel_list'] = personnel_list
        return render(request, 'rakun/classes/class_list.html', context)
    except Exception as e:
        print(e)


def set_new_class(request):
    try:
        print('.................classes/views/set_new_class function called')
        context = Authantication.getInstance().getUser()
        class_form = NewClassFrom(request.POST or None)
        context['form'] = class_form
        if class_form.is_valid():
            data_class = class_form.cleaned_data
            data_class['company_id'] = request.COOKIES.get('company_id')
            new_class = ClassService()
            result = new_class.save_class(data_class)
            if result.meta.id:
                messages.success(request, 'Sınıf sisteme kayıt edilmiştir.')
                return redirect('classes:set_new_class')
        return render(request, 'rakun/classes/set_new_class.html', context)
    except Exception as e:
        print(e)

def detail(request, class_id):
    try:
        context = Authantication.getInstance().getUser()
        get_all_students = StudentService().related_classes({'class_room': class_id, 'company_id': request.COOKIES.get('company_id')})
        context['class_name'] = get_all_students.hits.hits[0]['_source']['class_name']
        context['class_id'] = get_all_students.hits.hits[0]['_source']['class_room']
        context['page_data'] = get_all_students
        context['page'] = 'Sınıflar / ' + get_all_students.hits.hits[0]['_source']['class_name']
        return render(request, 'rakun/classes/detail.html', context)
    except Exception as e:
        print(e)


def update(request, class_id=None):
    try:
        print('.................classes/views/update function called')
        context = Authantication.getInstance().getUser()
        get_class = ClassService().find_by_id({'id': class_id})
        class_data = get_class.hits.hits[0]['_source']
        print('class_data', class_data)
        class_form = NewClassFrom(data=request.POST or None, initial=class_data)
        if class_form.is_valid():
            form_data = class_form.cleaned_data
            quota_control = form_data['quota'] - class_data['registered_student']
            if quota_control <= 0:
                messages.warning(request, 'Kota sınıf mevcudunun altında olamaz.')
            else:
                form_data['id'] = class_id
                update_class = ClassService().update(form_data)
                if update_class:
                    messages.success(request, 'Sınıf başarıyla güncellendi.')
        context['class_id'] = class_id
        context['edit_class_form'] = class_form
        return render(request, 'rakun/classes/edit.html', context)
    except Exception as e:
        print(e)


def delete(request, class_id):
    try:
        pass
    except Exception as e:
        print(e)

def related_class(request):
    try:
        context = Authantication.getInstance().getUser()
        user_info = context['all_data']
        all_class = ClassService().in_condition({'id': user_info.class_room})
        personnel_list = list()
        for i in all_class:
            get_pers = PersonnelService().related_class({'class_room': i.meta.id})
            for pers_data in get_pers:
                personnel_list.append(
                    (pers_data.user_name + ' ' + pers_data.user_surname, i.meta.id, pers_data.meta.id))
        context['personnel_list'] = personnel_list
        context['page_data'] = all_class
        context['class_name'] = 'ali'
        return render(request, 'rakun/classes/class_list.html', context)
    except Exception as e:
        print(e)


def inspection(request, class_id=None):
    try:
        context = Authantication.getInstance().getUser()
        user_info = context['all_data']
        if class_id is not None:
            get_all_students = StudentService().related_classes(
            {'class_room': class_id, 'company_id': request.COOKIES.get('company_id')})
            inspection_form = list()
            for i in get_all_students:
                i._d_['student_id'] = i.meta.id
                inspection_form.append(StudentInspectionForm(data=request.POST or None, initial=i._d_))
        else:
            inspection_form = StudentInspectionForm(data=request.POST)
            if inspection_form.is_valid():
                data = inspection_form.cleaned_data
                print('DATA: ', data)
        context['inspection_form'] = inspection_form
        return render(request, 'rakun/test.html', context)
    except Exception as e:
        print(e)
