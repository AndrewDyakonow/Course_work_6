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
    # mailing_name = forms.CharField(label='Название')
    # client_name = forms.CharField(label='Имя клиентов')
    # date_mailing = forms.DateTimeField(label='Дата начала рассылки')
    # date_end_mailing = forms.DateTimeField(label='Дата окончания рассылки')
    # periodicity = forms.CharField(label='Периодичность')
    # status = forms.CharField(label='Статус')

    class Meta:
        model = Settings
        fields = '__all__'


class MessagesCreateForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = '__all__'
