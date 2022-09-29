import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    if not domain:
        domain = 'cj.com'
    if not email_prefix:
        email_prefix = 'test_user'

    random_email_string = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string))
    email = f'{email_prefix}{random_string}@{domain}'

    password_length = 15
    password = ''.join(random.choices(string.ascii_letters, k=password_length))

    return {'email': email, 'password': password}


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))
