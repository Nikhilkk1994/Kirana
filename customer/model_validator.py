from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_mobile(value):
    value_len = len(str(value))
    if value_len < 10 or value_len > 10:
        raise ValidationError(_('Mobile number is correct'))
