import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


# Проверка на последовательности символов на одной строке клавиатуры
def in_keyboard(sub: str) -> bool:
    keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

    for row in keyboard_rows:
        if sub in row or sub in row[::-1]:
            return True
    return False


# Валидация пароля
def validate_password(value):
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



def validate_phone_number(phone_number: str):
    phone_regex_dict = {
        ('+7', '+33', '+34', '+90', '+30', '+351', '+212', '+213', '+216', '+380', '+375'): r'\d{3}\d{3}\d{2}\d{2}',
        # xxx xxx xx xx
        ('+1', '+49', '+39', '+86', '+55', '+52', '+61', '+91', '+54', '+92', '+82', '+81', '+27', '+63', '+62', '+84',
         '+57', '+51', '+56', '+593', '+58', '+66', '+98', '+60', '+234', '+355'): r'\d{3}\d{3}\d{4}',  # xxx xxx xxxx
        ('+44', '+353', '+31', '+46', '+47', '+358', '+45', '+41', '+43', '+64'): r'\d{4}\d{3}\d{3}',  # xxxx xxx xxx
        ('+972', '+65', '+852', '+354', '+372', '+371', '+370'): r'\d{2}\d{4}\d{4}',  # xx xxxx xxxx
        ('+32', '+420', '+421', '+48', '+40', '+36'): r'\d{2}\d{3}\d{4}',  # xx xxx xxxx
        ('+385', '+386', '+358'): r'\d\d{3}\d{3}\d{3}',  # x xxx xxx xxx
        ('+45', '+47', '+354'): r'\d{2}\d{2}\d{2}\d{2}',  # xx xx xx xx
        ('+33', '+352', '+370', '+41'): r'\d{3}\d{2}\d{2}\d{2}',  # xxx xx xx xx
    }
    for prefixes, regex in phone_regex_dict.items():
        for prefix in prefixes:
            if phone_number.startswith(prefix):
                # Убираем префикс из номера для последующей проверки
                local_number = phone_number[len(prefix):]
                match = re.fullmatch(pattern=regex, string=local_number)
                if not match:
                    raise ValidationError(f'Неверный формат номера для префикса {prefix}.')
                return

    # Если ни один префикс не совпал
    raise ValidationError('Некорректный префикс номера.')


def validate_image(image):
    # Проверка размера файла
    filesize = image.file.size
    if filesize > 4 * 1024 * 1024:  # 4 MB
        raise ValidationError(_('Размер файла не должен превышать 4MB.'))

    # Проверка разрешения изображения
    img = Image.open(image)
    width, height = img.size
    if width > 200 or height > 200:
        raise ValidationError(_('Разрешение изображения не должно превышать 200x200 пикселей.'))
