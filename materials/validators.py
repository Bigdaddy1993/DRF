import re

from rest_framework.serializers import ValidationError


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^https://www.youtube.com/')
        tmp_val = dict(value).get(self.field)
        if tmp_val is None:
            return 'null'
        if not bool(reg.match(tmp_val)):
            raise ValidationError('ссылка должна быть на ютуб')

