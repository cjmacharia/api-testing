from src.utilities.genericUtilities import generate_random_email_and_password
from src.utilities.requestUtility import RequestUtility


class CustomerHelper(object):
    def __init__(self):
        self.request_utility = RequestUtility()

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            info = generate_random_email_and_password()
            email = info['email']
        if not password:
            password = 'password1'
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        return self.request_utility.post('customers', payload)
