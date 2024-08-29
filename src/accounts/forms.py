from django import forms
from accounts.models.user import CustomUser
from accounts.models.profile import Profile
from accounts.validators import validate_password
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _


# форма для регистрации
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput(), label=_('Подтверждение пароля'))
    code_word = forms.CharField(widget=forms.PasswordInput(), max_length=12, required=False,
                                label=_('Кодовое слово(необязательно)'))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'code_word']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Пароли не совпадают'))
        return password2


# форма для входа
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


# форма для верификации кода из почты
'''
class CodeVerificationForm(forms.Form):
    verification_code = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'Введите код'}),
        label='Код верификации'
    )
'''


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'city', 'description', 'photo_url']
