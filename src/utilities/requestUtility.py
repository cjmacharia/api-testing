import json
import os

import requests

from src.configs.host_config import API_HOST
from requests_oauthlib import OAuth1

from src.utilities.credentialsUtility import get_wc_api_keys


class RequestUtility(object):
    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOST[self.env]
        self.status_code = None
        self.expected_status_code = None
        self.wc_creds = get_wc_api_keys()
        self.auth = OAuth1(self.wc_creds['wc_key'],
                           self.wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f"incorrect status code: Expected {self.expected_status_code} Actual {self.status_code}"

    def post(self, endpoint, payload, headers=None, expected_status_code=201):
        if not headers:
            headers = {"content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        return rs_api.json()

    def get(self, endpoint=None, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.get(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.assert_status_code()
        return rs_api.json()
