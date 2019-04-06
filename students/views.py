from django.shortcuts import render
from Context.ContextView import Authantication
from students.service import StudentService

# Create your views here.

def index(request):
    try:
        print('.................personnels/views/index function called')
        context = Authantication.getInstance().getUser()
        context['page'] = 'Öğrenciler'
        all_students = StudentService().get_all_student({'company_id': request.COOKIES.get('company_id')})
        context['page_data'] = all_students
        return render(request, 'rakun/students/student_list.html', context)
    except Exception as e:
        print(e)
