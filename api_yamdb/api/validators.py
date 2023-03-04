import re
from django.core.exceptions import ValidationError


def username_validator(value):
    symbol = re.sub(r'[\w.@+-]', '', value)
    if value == 'me':
        raise ValidationError(
            'Имя "me" в качестве username запрещено')
    elif value in symbol:
        raise ValidationError(
            f'Запрещено использование {symbol} в имени')
    return value
