from django import forms
import datetime
import calendar

years_choices = [(r,r) for r in range(1974, datetime.date.today().year+1)]
days_choices = [(r,r) for r in range(1, 32)]
months_choices = [(r,calendar.month_name[r]) for r in range(1, 13)]
position_choices = [
    ('1', 'Öğretmen'),
    ('2', 'İdari Personel'),
    ('3', 'Teknik Personel')
]
class_room_choices = [
    ('zipirlar', 'Zıpırlar'),
    ('rakunlar', 'Rakunlar'),
    ('anarsistler', 'Anarşistler'),
    ('penguenler', 'Penguenler'),
]
authorization_choices = (
    ('pers_views', 'Personel listesini görüntüleyebilsin'),
    ('pers_write', 'Yeni personel ekleyebilsin.'),
    ('pers_delete', 'Sistemde kayıtlı personelleri silebilsin.'),
)


class NewPersonnelForm(forms.Form):

    user_name = forms.CharField(max_length=20, required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control required',
                                    'id': 'user_name',
                                    'placeholder': 'Personel ismini girin'
                                }))
    user_surname = forms.CharField(max_length=20, required=True,
                                    widget=forms.TextInput(attrs={
                                    'class': 'form-control required',
                                    'id': 'user_surname',
                                    'placeholder': 'Personel soyismini girin'
                                    }))
    mail = forms.EmailField(max_length=50, required=True,
                            widget=forms.EmailInput(attrs={
                                'class': 'form-control required',
                                'id': 'mail',
                                'placeholder': 'example@email.com'
                            }))
    phone_number = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control required',
                                       'id': 'phone_number',
                                       'placeholder': '545 XXX XXXX',
                                       'data-mask': '999-999-9999',
                                   }))
    birth_month = forms.CharField(required=False,
                                  widget=forms.Select(choices=months_choices, attrs={
                                      'class': 'form-control form-control-select2',
                                      'data-placeholder': 'Ay',
                                  }))
    birth_day = forms.CharField(required=False,
                                  widget=forms.Select(choices=days_choices, attrs={
                                      'class': 'form-control form-control-select2',
                                      'data-placeholder': 'Gün',
                                  }))
    birth_year = forms.CharField(required=False,
                                  widget=forms.Select(choices=years_choices, attrs={
                                      'class': 'form-control form-control-select2',
                                      'data-placeholder': 'Yıl',
                                  }))
    address = forms.CharField(required=True, label='İkamet adresi',
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control required',
                                  'row': '2',
                                  'cols': '3',
                                  'placeholder': 'Personel adresini giriniz.'
                              }))
    university = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'university',
                                    'placeholder': 'Mezun olduğu üniversite'
                                }))
    domain = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'domain',
                                    'placeholder': 'Tamaladığı bölüm'
                                }))
    language = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'language',
                                    'placeholder': 'İngilizce, Almanca vs'
                                }))
    personnel_education_from_month = forms.CharField(required=False, widget=forms.Select(choices=months_choices, attrs={
                                      'class': 'form-control form-control-select2',
                                      'data-placeholder': 'Ay',
                                  }))
    personnel_education_from_year = forms.CharField(required=False, widget=forms.Select(choices=years_choices, attrs={
                                      'class': 'form-control form-control-select2',
                                      'data-placeholder': 'Yıl',
                                  }))
    position = forms.CharField(required=False, widget=forms.Select(choices=position_choices, attrs={
                                      'class': 'form-control form-control-select2 required',
                                      'data-placeholder': 'Hangi pozisyonda görevlendirilecek',
                                  }))
    class_room = forms.CharField(required=False, widget=forms.SelectMultiple(choices=class_room_choices, attrs={
                                      'class': 'form-control form-control-select2 required',
                                      'data-placeholder': 'Ders vereceği sınılar',
                                  }))
    pers_view = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
                                      'class': 'custom-control-input',
                                      'id': 'custom_checkbox_stacked_unchecked_1',
                                        'checked': 'checked'
                                  }))
    pers_write = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_1',
    }))
    pers_delete = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_2',
    }))
    parent_views = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_unchecked_2',
        'checked': 'checked'
    }))
    parent_write = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_3',
    }))
    parent_delete = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_4',
    }))
    student_views = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_unchecked_3',
        'checked': 'checked'
    }))
    student_write = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_5',
    }))
    student_delete = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_6',
    }))
    administrative_view = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_unchecked_4',
        'checked': 'checked'
    }))
    administrative_write = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_7',
    }))
    administrative_delete = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input',
        'id': 'custom_checkbox_stacked_checked_8',
    }))

    def clean(self):
        user_name = self.cleaned_data.get('user_name')
        user_surname = self.cleaned_data.get('user_surname')
        mail = self.cleaned_data.get('mail')
        phone_number = self.cleaned_data.get('phone_number')
        birth_month = self.cleaned_data.get('birth_month')
        birth_day = self.cleaned_data.get('birth_day')
        birth_year = self.cleaned_data.get('birth_year')
        address = self.cleaned_data.get('address')
        university = self.cleaned_data.get('university')
        domain = self.cleaned_data.get('domain')
        language = self.cleaned_data.get('language')
        personnel_education_from_month = self.cleaned_data.get('personnel_education_from_month')
        personnel_education_from_year = self.cleaned_data.get('personnel_education_from_year')
        position = self.cleaned_data.get('position')
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
            'birth_month': birth_month,
            'birth_day': birth_day,
            'birth_year': birth_year,
            'address': address,
            'university': university,
            'domain': domain,
            'language': language,
            'personnel_education_from_month': personnel_education_from_month,
            'personnel_education_from_year': personnel_education_from_year,
            'position': position,
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
