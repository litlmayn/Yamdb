import re
from django.core.exceptions import ValidationError


def username_validator(value):
    s = re.sub(r'[\w.@+-]', '', value)
    symbol = ''.join(set(s))
    if value == 'me':
        raise ValidationError(
            'Имя "me" в качестве username запрещено')
    if symbol:
        raise ValidationError(
            f'Запрещено использование {symbol} в имени')
    return value
