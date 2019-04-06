from django import forms
from classes.service import ClassService


class NewPersonnelForm(forms.Form):

    def __init__(self, request=None, *args, **kwargs):
        super(NewPersonnelForm, self).__init__(*args, **kwargs)
        data = {'company_id': request}
        all_class = ClassService().get_all_class(data)
        if all_class is not None:
            classes_choices = [(i.meta.id, i.class_name) for i in all_class]
            self.fields['class_room'].choices = classes_choices
        else:
            self.fields['class_room'].choices = [('0', '---------')]

    classes_choices = [('0', '---------')]

    personnel_choices = [
        ('1', 'Öğretmen'),
        ('2', 'İdari Personel'),
        ('3', 'Teknik Personel')
    ]

    user_name = forms.CharField(
        max_length=20,
        required=True,
        label='Personel ismi',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_name',
                'placeholder': 'Personel ismini girin'
            }))
    user_surname = forms.CharField(
        max_length=20,
        required=True,
        label='Personel soyisim',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_surname',
                'placeholder': 'Personel soyismini girin'
            }))
    mail = forms.EmailField(
        max_length=50,
        required=True,
        label='Mail adresi',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control required',
                'id': 'mail',
                'placeholder': 'example@email.com'
            }))
    phone_number = forms.CharField(
        required=True,
        label='Telefon numarası',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'phone_number',
                'placeholder': '545 XXX XXXX',
                'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}'
            }))
    birth_date = forms.DateField(
        required=False,
        label='Doğum Tarihi',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'name': 'date',
                'type': 'date'
            }))
    address = forms.CharField(
        required=True,
        label='İkamet adresi',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'row': '2',
                'cols': '3',
                'placeholder': 'Personel adresini giriniz.'
            }))
    university = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'university',
                'placeholder': 'Mezun olduğu üniversite'
            }))
    personnel_type = forms.CharField(
        required=False,
        widget=forms.Select(
            choices=personnel_choices,
            attrs={
                'class': 'form-control form-control-select2 required',
                'data-placeholder': 'Hangi pozisyonda görevlendirilecek',
            }))
    class_room = forms.MultipleChoiceField(
        required=False,
        choices=classes_choices,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control multiselect',
                'multiple': 'multiple'
            }))
    pers_view = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_unchecked_1',
                'checked': 'checked'
            }))
    pers_write = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_1',
            }))
    pers_delete = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_2',
            }))
    parent_views = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_unchecked_2',
                'checked': 'checked'
            }))
    parent_write = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_3',
            }))
    parent_delete = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_4',
            }))
    student_views = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_unchecked_3',
                'checked': 'checked'
            }))
    student_write = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_5',
            }))
    student_delete = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_6',
            }))
    administrative_view = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_unchecked_4',
                'checked': 'checked'
            }))
    administrative_write = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_7',
            }))
    administrative_delete = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_8',
            }))

    def clean(self):
        user_name = self.cleaned_data.get('user_name')
        user_surname = self.cleaned_data.get('user_surname')
        mail = self.cleaned_data.get('mail')
        phone_number = self.cleaned_data.get('phone_number')
        birth_date = self.cleaned_data.get('birth_date')
        address = self.cleaned_data.get('address')
        university = self.cleaned_data.get('university')
        personnel_type = self.cleaned_data.get('personnel_type')
        class_room = self.cleaned_data.get('class_room')
        pers_view = self.cleaned_data.get('pers_view')
        pers_write = self.cleaned_data.get('pers_write')
        pers_delete = self.cleaned_data.get('pers_delete')
        parent_views = self.cleaned_data.get('parent_views')
        parent_write = self.cleaned_data.get('parent_write')
        parent_delete = self.cleaned_data.get('parent_delete')
        student_views = self.cleaned_data.get('student_views')
        student_write = self.cleaned_data.get('student_write')
        student_delete = self.cleaned_data.get('student_delete')
        administrative_view = self.cleaned_data.get('administrative_view')
        administrative_write = self.cleaned_data.get('administrative_write')
        administrative_delete = self.cleaned_data.get('administrative_delete')

        values = {
            'user_name': user_name,
            'user_surname': user_surname,
            'mail': mail,
            'phone_number': phone_number,
            'birth_date': birth_date,
            'address': address,
            'university': university,
            'personnel_type': personnel_type,
            'class_room': class_room,
            'pers_view': pers_view,
            'pers_write': pers_write,
            'pers_delete': pers_delete,
            'parent_views': parent_views,
            'parent_write': parent_write,
            'parent_delete': parent_delete,
            'student_views': student_views,
            'student_write': student_write,
            'student_delete': student_delete,
            'administrative_view': administrative_view,
            'administrative_write': administrative_write,
            'administrative_delete': administrative_delete,
        }

        return values



