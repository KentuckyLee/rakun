from django import forms
from users.services import UsersService

class UserAccountSetting(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Cep Telefonunuz (545 xxx xxxx)',
            'id': 'phone_number',
            'readonly': 'readonly'
        }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifrenizi tekrar girin',
            'id': 'password',
        }))

    password_replace = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifrenizi tekrar girin',
            'id': 'password_replace',
        }))

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        password_replace = self.cleaned_data.get('password_replace')
        if password != password_replace:
            raise forms.ValidationError('Girilen şifreler eşleşmiyor')

        values = {
            'phone_number': phone_number,
            'password': password,
            'password_replace': password_replace
        }

        return values
