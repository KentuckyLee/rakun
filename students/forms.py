from django import forms
from classes.service import ClassService


class NewStudentForm(forms.Form):

    def __init__(self, request=None, *args, **kwargs):
        super(NewStudentForm, self).__init__(*args, **kwargs)
        data = {'company_id': request}
        all_class = ClassService().get_all_class(data)
        if all_class is not None:
            classes_choices = [(i.meta.id, i.class_name + ' ' + '(' + str(i.quota) + '/ ' + str(i.registered_student) +')') for i in all_class]
            self.fields['class_room'].widget.choices = classes_choices
        else:
            self.fields['class_room'].choices = [('0', '---------')]

    classes_choices = [('0', '---------')]
    student_name = forms.CharField(
        max_length=20,
        required=True,
        label='Öğrenci ismi ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_name',
                'placeholder': 'Öğrenci ismini girin'
            }))
    student_surname = forms.CharField(
        max_length=20,
        required=True,
        label='Öğrenci soyisim',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_surname',
                'placeholder': 'Öğrenci soyismini girin'
            }))
    student_birth_date = forms.DateField(
        required=False,
        label='Doğum Tarihi',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'name': 'date',
                'type': 'date',
                'placeholder': 'Öğrencinin doğum tarihini girin'
            }))
    private_student = forms.BooleanField(
        required=False,
        label='Özel öğrenci statusunde mi?',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_unchecked_1'
            }))
    class_room = forms.CharField(
        required=True,
        widget=forms.Select(
            choices=classes_choices,
            attrs={
                'class': 'form-control form-control-select2 required',
            }))
    student_note = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control required',
                'id': 'note',
                'placeholder': 'Öğrenciye ozel not girin',
                'rows': 2,
            }))

    def clean(self):
        student_name = self.cleaned_data.get('student_name')
        student_surname = self.cleaned_data.get('student_surname')
        student_birth_date = self.cleaned_data.get('student_birth_date')
        private_student = self.cleaned_data.get('private_student')
        class_room = self.cleaned_data.get('class_room')
        student_height = self.cleaned_data.get('student_height')
        student_weight = self.cleaned_data.get('student_weight')
        student_note = self.cleaned_data.get('student_note')

        values = {
            'student_name': student_name,
            'student_surname': student_surname,
            'student_birth_date': student_birth_date,
            'private_student': private_student,
            'class_room': class_room,
            'student_height': student_height,
            'student_weight': student_weight,
            'student_note': student_note
        }

        return values

class StudentInspectionForm(forms.Form):
    in_here = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_1',
            }))
    student_id = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.HiddenInput(
            attrs={
                'class': 'form-control required',
                'readonly': 'readonly'
            }))
    class_room = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.HiddenInput(
            attrs={
                'class': 'form-control required',
                'readonly': 'readonly'
            }))
    student_name = forms.CharField(
        max_length=20,
        required=True,
        label='Öğrenci ismi ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_name',
                'placeholder': 'Öğrenci ismini girin',
                'readonly': 'readonly'
            }))
    student_surname = forms.CharField(
        max_length=20,
        required=True,
        label='Öğrenci soyisim',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_surname',
                'placeholder': 'Öğrenci soyismini girin',
                'readonly': 'readonly'
            }))
    text = forms.CharField(
        required=True,
        label='Bilgilendirme',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control required',
                'rows': '4',
                'placeholder': 'Mesajını giriniz'
            }))

    def clean(self):
        student_name = self.cleaned_data.get('student_name')
        student_surname = self.cleaned_data.get('student_surname')
        in_here = self.cleaned_data.get('in_here')
        text = self.cleaned_data.get('text')
        student_id = self.cleaned_data.get('student_id')
        class_room = self.cleaned_data.get('class_room')

        values = {
            'student_name': student_name,
            'student_surname': student_surname,
            'in_here': in_here,
            'text': text,
            'student_id': student_id,
            'class_room': class_room
        }

        return values
