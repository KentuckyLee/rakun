from django import forms

class NewClassFrom(forms.Form):
    class_name = forms.CharField(
        max_length=50,
        required=True,
        label='Sınıf ismi',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'class_name',
                'placeholder': 'Sınıfın ismini girin'
            }))
    quota = forms.IntegerField(
        max_value=250,
        min_value=0,
        label='Sınıf kontenjanı',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'quota',
                'placeholder': 'Sınıfın ismini girin'
            }))
    quota_check = forms.BooleanField(
        required=True,
        label='Sınıfın kontenjanını belirlemek istiyor musunuz?',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input',
                'id': 'custom_checkbox_stacked_checked_1',
                'checked': 'checked'
            }))

    def clean(self):
        class_name = self.cleaned_data.get('class_name')
        quota = self.cleaned_data.get('quota')
        quota_check = self.cleaned_data.get('quota_check')

        values = {
            'class_name': class_name,
            'quota': quota,
            'quota_check': quota_check
        }

        return values
