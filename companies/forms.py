from django import forms


class RegisterForm(forms.Form):

    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Cep Telefonunuz (545 xxx xxxx)',
            'id': 'register_phone',
            'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}'
        }))
    phone_replace = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Cep Telefonunuz (545 xxx xxxx)',
            'id': 'register_phone_replace',
            'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}'
        }))
    company = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Anaokul adını giriniz',
            'id': 'register_company',
        }))
    user_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'İsminiz',
            'id': 'user_name',
        }))
    user_surname = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Soyisminiz',
            'id': 'user_surname',
        }))
    mail = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Mail adresiniz',
            'id': 'register_mail',
        }))

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_replace = self.cleaned_data.get('phone_replace')
        company = self.cleaned_data.get('company')
        user_name = self.cleaned_data.get('user_name')
        user_surname = self.cleaned_data.get('user_surname')
        mail = self.cleaned_data.get('mail')

        if phone_number != phone_replace:
            raise forms.ValidationError('Girilen telefon numaraları eşleşmiyor')

        values = {
            'phone_number': phone_number,
            'company': company,
            'user_name': user_name,
            'user_surname': user_surname,
            'mail': mail
        }

        return values


class LoginForm(forms.Form):

    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Cep Telefonunuz (545 xxx xxxx)',
            'id': 'phone_number',
            'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}'
        }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifreniz',
            'id': 'password',
        }))

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')

        values = {
            'phone_number': phone_number,
            'password': password
        }

        return values


class NewPasswordForm(forms.Form):

    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Cep Telefonunuz (545 xxx xxxx)',
            'id': 'phone_number',
            'pattern': '[0-9]{3}[0-9]{3}[0-9]{4}'
        }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifreniz',
            'id': 'password',
        }))

    password_replace = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifrenizi tekrar girin',
            'id': 'password_replace',
        }))

    # company_id = forms.CharField(widget=forms.HiddenInput(
    #     attrs={
    #         'id': 'company_id',
    #         'value': '{{company_id}}'
    #     }
    # ))

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        password_replace = self.cleaned_data.get('password_replace')
        # company_id = self.cleaned_data.get('company_id')
        if password != password_replace:
            raise forms.ValidationError('Girilen şifreler eşleşmiyor')

        values = {
            'phone_number': phone_number,
            'password': password,
            'password_replace': password_replace,
            # 'company_id': company_id
        }

        return values
