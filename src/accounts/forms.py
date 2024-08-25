from django import forms
from accounts.models.user import CustomUser
from accounts.models.profile import Profile
from accounts.validators import validate_password, validate_phone_number
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Подтверждение пароля')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Пароли не совпадают'))
        return password2


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'city_name', 'description', 'photo_url']
