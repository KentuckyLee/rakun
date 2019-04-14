from django import forms
from users.services import UsersService

class SendNotificationForm(forms.Form):

    def __init__(self, request=None, *args, **kwargs):
        super(SendNotificationForm, self).__init__(*args, **kwargs)
        data = {'company_id': request}
        all_user = UsersService().get_all_user(data)
        if all_user is not None:
            users_choices = [('1', 'Tüm kullanıcılar'), ('2', 'Tüm Personeller'), ('3', 'Tüm Veliler')]
            data = [(i.meta.id, i.user_name + ' ' + i.user_surname) for i in all_user]
            for i in data:
                users_choices.append(i)
            self.fields['user_list'].choices = users_choices
        else:
            self.fields['user_list'].choices = [('1', 'Tüm kullanıcılar'), ('2', 'Tüm Personeller'), ('3', 'Tüm Veliler')]

    users_choices = [('1', 'Tüm kullanıcılar'), ('2', 'Tüm Personeller'), ('3', 'Tüm Veliler')]
    user_list = forms.MultipleChoiceField(
        required=False,
        choices=users_choices,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control multiselect',
                'multiple': 'multiple'
            }))

    text = forms.CharField(
        required=True,
        label='Bildiriminiz',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control required',
                'rows': '4',
                'placeholder': 'Mesajını giriniz'
            }))

    def clean(self):
        user_list = self.cleaned_data.get('user_list')
        text = self.cleaned_data.get('text')
        values = {
            'user_list': user_list,
            'text': text,
        }
        return values
