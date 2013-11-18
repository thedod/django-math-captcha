# -*- coding: utf-8 -*-
from django.conf import settings

NUMBERS = getattr(settings, 'MATH_CAPTCHA_NUMBERS', xrange(1,6))
OPERATORS = getattr(settings, 'MATH_CAPTCHA_OPERATORS', '+*') # Known bug: in rtl languages don't use - or /
