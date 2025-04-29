"""
Expresiones regulares de módulo re
"""

import re

# validación de email


def validate_email(email):
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email))


print(validate_email("mjt20@yavirac.com"))

# validación de phone

def validate_phone(phone):
    return bool(re.match(r"^\+?[0-9]{10}+$", phone))


print(f"Bool:{validate_phone('0995377872')}")

# validación de url

def validate_url(url):
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{3}+$", url))


print(f"Bool:{validate_url('https://www.google.com')}")
