import random

from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from course_work.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, VerificationForm, UserRecoveryForm, UserProfileForm
from users.models import Users


# Create your views here.


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        a = Users.objects.get(email=self.request.user)
        if a.is_activated:
            return reverse_lazy('servises:main_page')
        return reverse_lazy('users:verify')


class LogoutView(auth_views.LogoutView):
    template_name = 'users/login.html'


class RegisterView(CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form, **kwargs):
        mail = form.cleaned_data.get('email')
        my_token = random.randint(1000000, 9999999)
        send_mail(
            'Регистрация',
            f'Для регистрации введите код {my_token}',
            settings.EMAIL_HOST_USER,
            recipient_list=[mail],
        )
        form.instance.mytoken = my_token
        form.save()
        return super().form_valid(form)


class VerificationsView(UpdateView):
    model = Users
    form_class = VerificationForm
    template_name = 'users/verification.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tocken = None

    def form_valid(self, form):
        self.tocken = form.cleaned_data.get('secretkey')
        a = Users.objects.get(email=self.request.user)

        if self.tocken == a.mytoken:
            form.instance.is_activated = True

        form.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        a = Users.objects.get(email=self.request.user)
        if a.is_activated:
            return reverse_lazy('servises:main_page')
        return reverse_lazy('users:verify')


class PasswordRecoveryView(PasswordResetView):
    template_name = 'users/signin.html'
    subject_template_name = 'users/title.txt',
    email_template_name = 'users/body.txt',
    success_url = reverse_lazy('servises:main_page')  # !!!!!!!
    from_email = EMAIL_HOST_USER
    form_class = UserRecoveryForm


class PasswordResetView(PasswordResetConfirmView):
    post_reset_login = True
    success_url = reverse_lazy('servises:main_page')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Users
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


# LoginRequiredMixin,