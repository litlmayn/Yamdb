import datetime as dt

from django.core.exceptions import ValidationError


def year_validator(value):
    if value > int(dt.datetime.now().year):
        raise ValidationError(
            'Год больше текущего'
        )
