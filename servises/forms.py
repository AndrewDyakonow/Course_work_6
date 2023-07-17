from django import forms

from servises.models import Client, Settings, Messages


class ClientCreateForm(forms.ModelForm):

    name = forms.CharField(label='ФИО')
    email = forms.EmailField(label='email')
    comment = forms.CharField(label='Комментарий')

    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)


class SettingCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget = forms.HiddenInput()

    class Meta:
        model = Settings
        fields = '__all__'


class MessagesCreateForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = '__all__'
