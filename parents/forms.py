from django import forms


class NewParentForm(forms.Form):
    user_name = forms.CharField(
        max_length=50,
        required=True,
        label='Veli ismi',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_name',
                'placeholder': 'Personel ismini girin'
            }))
    user_surname = forms.CharField(
        max_length=20,
        required=True,
        label='Veli soyisim',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_surname',
                'placeholder': 'Personel soyismini girin'
            }))
    mail = forms.EmailField(
        max_length=50,
        required=False,
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
        label='Velinin Doğum Tarihi',
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
                'rows': '2',
                'placeholder': 'Veli adresini giriniz.'
            }))
    students_count = forms.IntegerField(
        required=True,
        max_value=100,
        min_value=0,
        label='Kaydedilecek öğrenci sayısı',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'name': 'height',
                'placeholder': 'Kaydedilecek Öğrenci sayısı'
            }))

    def clean(self):
        user_name = self.cleaned_data.get('user_name')
        user_surname = self.cleaned_data.get('user_surname')
        mail = self.cleaned_data.get('mail')
        phone_number = self.cleaned_data.get('phone_number')
        birth_date = self.cleaned_data.get('birth_date')
        students_count = self.cleaned_data.get('students_count')
        address = self.cleaned_data.get('address')

        values = {
            'user_name': user_name,
            'user_surname': user_surname,
            'mail': mail,
            'phone_number': phone_number,
            'birth_date': birth_date,
            'students_count': students_count,
            'address': address
        }
        return values

class EditParentFrom(forms.Form):
    user_name = forms.CharField(
        max_length=50,
        required=True,
        label='Veli ismi',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_name',
                'placeholder': 'Personel ismini girin'
            }))
    user_surname = forms.CharField(
        max_length=20,
        required=True,
        label='Veli soyisim',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control required',
                'id': 'user_surname',
                'placeholder': 'Personel soyismini girin'
            }))
    mail = forms.EmailField(
        max_length=50,
        required=False,
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
        label='Velinin Doğum Tarihi',
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
                'rows': '2',
                'placeholder': 'Veli adresini giriniz.'
            }))

    def clean(self):
        user_name = self.cleaned_data.get('user_name')
        user_surname = self.cleaned_data.get('user_surname')
        mail = self.cleaned_data.get('mail')
        phone_number = self.cleaned_data.get('phone_number')
        birth_date = self.cleaned_data.get('birth_date')
        address = self.cleaned_data.get('address')

        values = {
            'user_name': user_name,
            'user_surname': user_surname,
            'mail': mail,
            'phone_number': phone_number,
            'birth_date': birth_date,
            'address': address
        }
        return values
