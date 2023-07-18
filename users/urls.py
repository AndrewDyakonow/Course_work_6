from django.urls import path

from users.views import LoginView, LogoutView, RegisterView, VerificationsView, PasswordRecoveryView, PasswordResetView, \
    ProfileView

app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('veryfy/', VerificationsView.as_view(), name='verify'),

    path('recovery/', PasswordRecoveryView.as_view(), name='recovery'),
    path('reset/<uidb64>/<token>/', PasswordResetView.as_view(), name='reset'),
    path('register/send/', RegisterView.as_view(), name='register_send'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
