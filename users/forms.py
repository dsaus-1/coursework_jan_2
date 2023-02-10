from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, ReadOnlyPasswordHashField, \
    PasswordChangeForm, PasswordResetForm, SetPasswordForm

from mailing.forms_mixins import StyleFormMixin
from users.models import User
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class CustomRegisterUserForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country')


class CustomEditUserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone', 'country')

class CustomPasswordChangeForm(StyleFormMixin, PasswordChangeForm):
    pass

class CustomPasswordResetForm(StyleFormMixin, PasswordResetForm):
    pass

class CustomSetPasswordForm(StyleFormMixin, SetPasswordForm):
    pass