import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Проверка на последовательности символов на одной строке клавиатуры
def in_keyboard(sub: str) -> bool:
    keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    for row in keyboard_rows:
        if sub in row or sub in row[::-1]:
            return True
    return False


# Валидация пароля
def validate_password(value):
    print("Проверка пароля")
    # Проверка длины
    if len(value) < 8:
        raise ValidationError(_('Пароль должен быть не менее 8 символов.'))

    # Проверка на содержание только букв и чисел
    if not re.match('^[A-Za-z0-9]*$', value):
        raise ValidationError(_('Пароль может содержать только буквы и цифры.'))

    # Проверка наличия хотя бы одной заглавной буквы
    if not re.search('[A-Z]', value):
        raise ValidationError(_('Пароль должен содержать хотя бы одну заглавную букву.'))

    # Подстроки по 4 символов
    substrings = [value[i:i + 4] for i in range(len(value) - 3)]

    # Проверка находится ли не правильная последовательность
    if any(in_keyboard(sub.lower()) for sub in substrings):
        raise ValidationError('Invalid substring found.')


# Валидация возраста
def validate_age(value: int):
    if value < 0:
        raise ValidationError(_('Возраст не может быть отрицательным.'))


# Валидация города
def validate_city(value: str):
    # Проверка на то не пуста ли значение и содержит ли заглавную букву
    if value and not value[0].isupper():
        raise ValidationError(_('Первая буква должна быть заглавной.'))


def validate_phone_number(value: str):
    ...
    # # Убираем все нецифровые символы, кроме '+'
    # digits = re.sub(r'[^\d+]', '', value)
    #
    # # Проверяем длину номера и то что номер состоит только из цифр и опционального '+'
    # if len(digits) < 7 or len(digits) > 16 or not re.fullmatch(r'\+?\d{7,15}', digits):
    #     raise ValidationError(_('Не правильный формат номер телефона'))
