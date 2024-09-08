from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from profiles.models.profiles import Profile
from accounts.models.custom_user import CustomUser
from accounts.validators import validate_password
from accounts import messages


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        label=_("Почта"),
        error_messages={
            "invalid": _(messages.INVALID_EMAIL_ERROR_MESSAGE),
            "unique": _(messages.NOT_UNIQUE_EMAIL_ERROR_MESSAGE),
        },
    )
    password1 = serializers.CharField(
        write_only=True,
        validators=[validate_password],
        label=_("Пароль"),
    )
    password2 = serializers.CharField(
        write_only=True,
        label=_("Подтверждение пароля"),
    )
    code_word = serializers.CharField(
        max_length=12,
        required=False,
        label=_("Кодовое слово (необязательно)"),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "code_word"]
        labels = {
            "username": _("Имя пользователя"),
        }

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(_(messages.NOT_UNIQUE_EMAIL_ERROR_MESSAGE))
        return value

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_(messages.PASSWORDS_DONT_MATCH_ERROR_MESSAGE))
        return data
        
    def create(self, validated_data):                                 
        validated_data.pop("password2")
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password1"],
            code_word=validated_data.get("code_word", "")
        )
        return user



# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(
#         label=_("Почта"),
#         error_messages={
#             "invalid": _("Некорректный формат электронной почты"),
#             "required": _("Введите адрес электронной почты"),
#         },
#     )
#     password = serializers.CharField(
#         write_only=True,
#         label=_("Пароль"),
#         style={"input_type": "password"}
#     )


# class ProfileSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Profile
# 		fields = ["age", "city", "description", "photo_url"]
