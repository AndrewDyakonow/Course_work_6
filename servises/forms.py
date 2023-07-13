from django import forms

from servises.models import Client


class ClientCreateForm(forms.ModelForm):

    name = forms.CharField(label='ФИО')
    email = forms.EmailField(label='email')
    comment = forms.CharField(label='Комментарий')

    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)
