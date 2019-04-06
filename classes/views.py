from django.shortcuts import render, redirect
from django.contrib import messages
from Context.ContextView import Authantication
from classes.forms import NewClassFrom
from classes.service import ClassService


def index(request):
    try:
        print('.................classes/views/index function called')
        context = Authantication.getInstance().getUser()
        context['page'] = 'Sınıflar'
        all_class = ClassService().get_all_class(context)
        context['page_data'] = all_class
        return render(request, 'rakun/classes/class_list.html', context)
    except Exception as e:
        print(e)


def set_new_class(request):
    try:
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
