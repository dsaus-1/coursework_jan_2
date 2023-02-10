import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from services.users_serv.confirm_account import confirm_account
from users.forms import CustomAuthenticationForm, CustomRegisterUserForm, CustomEditUserForm, CustomPasswordChangeForm, \
    CustomPasswordResetForm, CustomSetPasswordForm
from users.models import User


class CustomLoginView(LoginView):
    """Авторизация"""
    template_name = 'users/user_login.html'
    form_class = CustomAuthenticationForm
    model = User


class CustomRegisterView(CreateView):
    """Создать пользователя"""
    model = User
    form_class = CustomRegisterUserForm
    success_url = f'/users/page_after_registration'


    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.token = secrets.token_urlsafe(18)[:15]
            confirm_account(self.object)
            self.object.save()
        return super().form_valid(form)

def page_after_registration(request):
    # if request.method == 'POST':
    #     obj = User.objects.filter(token=token)
    #     confirm_account(obj)
    return render(request, 'users/page_after_registration.html')

# TODO: сделать повторную отправку сообщения и автоудаление аккаунта
# def repeat_message(request, token):
#
#         return render(request, )

class UserEditProfileView(UpdateView):
    """Редактировать профиль"""
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user

class CustomPasswordChangeView(PasswordChangeView):
    """Смена пароля"""
    model = User
    success_url = '/'
    form_class = CustomPasswordChangeForm
    template_name = 'users/change_password.html'

def activate_user(request, token):
    """Подтверждение профиля после регистрации"""
    u = User.objects.filter(token=token).first()

    if u:
        u.is_active = True
        u.save()
        return redirect('/users/login')

    return render(request, 'users/user_not_found.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = '/users/password_reset_send_mail'
    form_class = CustomPasswordResetForm
    email_template_name = 'users/email_reset.html'
    from_email = settings.EMAIL_HOST_USER

def password_reset_send_mail(request):
    return render(request, 'users/password_reset_send_mail.html')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('users:password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'

