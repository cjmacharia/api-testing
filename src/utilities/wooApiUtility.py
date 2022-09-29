import os

from requests_oauthlib import OAuth1
from woocommerce import API

from src.configs.host_config import WOO_API_HOST
from src.utilities.credentialsUtility import get_wc_api_keys


class WooApiUtility:
    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOST[self.env]
        self.status_code = None
        self.expected_status_code = None
        self.wc_creds = get_wc_api_keys()
        self.wc_api = API(
            url=self.base_url,
            consumer_key=self.wc_creds['wc_key'],
            consumer_secret=self.wc_creds['wc_secret'],
            version=WOO_API_HOST['version']
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f"incorrect status code: Expected {self.expected_status_code} Actual {self.status_code}"

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wc_api.get(wc_endpoint, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        return rs_api.json()

    def post(self, wc_endpoint, data=None, expected_status_code=201):
        rs_api = self.wc_api.post(wc_endpoint, data=data)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        return rs_api.json()

    def put(self, wc_endpoint, data=None, expected_status_code=200):

        rs_api = self.wc_api.put(wc_endpoint, data)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        return rs_api.json()
