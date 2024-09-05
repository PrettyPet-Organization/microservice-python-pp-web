from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from accounts.models.custom_user import CustomUser
from accounts.validators import validate_password
from profiles.models.profiles import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label=_("Почта"),
        error_messages={
            "invalid": _("Некорректный формат электронной почты"),
            "required": _("Введите адрес электронной почты"),
        },
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(), validators=[validate_password], label=_("Пароль")
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), label=_("Подтверждение пароля")
    )
    code_word = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=12,
        required=False,
        label=_("Кодовое слово(необязательно)"),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "code_word"]
        labels = {
            "username": _("Имя пользователя"),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Пароли не совпадают"))
        return password2


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label=_("Почта"),
        error_messages={
            "invalid": _("Некорректный формат электронной почты"),
            "required": _("Введите адрес электронной почты"),
        },
    )
    password = forms.CharField(widget=forms.PasswordInput, label=_("Пароль"))


# форма для верификации кода из почты
"""
class CodeVerificationForm(forms.Form):
    verification_code = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'Введите код'}),
        label='Код верификации'
    )
"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["age", "city", "description", "photo_url"]
