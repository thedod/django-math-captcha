# -*- coding: utf-8 -*-
from django.conf import settings

NUMBERS = getattr(settings, 'MATH_CAPTCHA_NUMBERS', xrange(1,6))
OPERATORS = getattr(settings, 'MATH_CAPTCHA_OPERATORS', '-+')
QUESTION = getattr(settings, 'MATH_CAPTCHA_QUESTION', 'Are you human? ')
### e.g. MATH_CAPTCHA_I18N_QUESTIONS can be {'en':'Are you human? ','fr':'Êtes-vous humain? '}
### fallback is MATH_CAPTCHA_QUESTION (so you need it as well)
I18N_QUESTIONS = getattr(settings, 'MATH_CAPTCHA_I18N_QUESTIONS', {})
