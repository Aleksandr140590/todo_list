import re


def validate_date(date):
    """Валидация введенных данных в атрибуты 'start' & 'end'"""
    return re.fullmatch(
        r"^((0[1-9]|[12]\d)\.(0[1-9]|1[012])|"
        r"30\.(0[13-9]|1[012])|31\.(0[13578]|1[02]))\.\d\d$",
        date
    )
