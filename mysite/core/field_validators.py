from django.core.validators import RegexValidator


ONLY_LETTERS_VALIDATOR = RegexValidator(
    regex=r'^[a-zA-Z]*$',
    message='Поле должно содержать только буквы',
    code='invalid_data'
)