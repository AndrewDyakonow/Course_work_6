from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm

from users.models import Users


class FormLogin(forms.ModelForm):
    model = Users


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ('email', 'password1', 'password2', 'mytoken')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mytoken'].widget = forms.HiddenInput()


class VerificationForm(forms.ModelForm):
    secretkey = forms.CharField(max_length=100, label='Секретный ключ')

    class Meta:
        model = Users
        fields = ('email',)


class UserRecoveryForm(PasswordResetForm):
    email = forms.EmailField(max_length=100)


class UserProfileForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
