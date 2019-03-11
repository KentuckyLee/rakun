from django.shortcuts import render
from personnel.forms import NewPersonnelForm


# Create your views here.


def index(request):

    return render(request, 'rakun/personnel_list.html')


def set_new_personnel(request):

    form = NewPersonnelForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        # user_name = form.cleaned_data.get('user_name')
        # user_surname = form.cleaned_data.get('user_surname')
        # mail = form.cleaned_data.get('mail')
        # phone_number
        # birth_month
        # birth_day
        # birth_year
        # address
        # university
        # domain
        # language
        # personnel_education_from_month
        # personnel_education_from_year
        # position
        # class_room
        # pers_view
        # pers_write
        # pers_delete
        # parent_views
        # parent_write
        # parent_delete
        # student_views
        # student_write
        # student_delete
        # administrative_view
        # administrative_write
        # administrative_delete
        context = {'data': data}
        return render(request, 'rakun/test.html', context)
    context = {
        'form': form,
    }
    return render(request, 'rakun/set_new_personnel.html', context)
