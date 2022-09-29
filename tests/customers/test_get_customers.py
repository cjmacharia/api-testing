import logging

import pytest

from src.utilities.requestUtility import RequestUtility


@pytest.mark.text03
def test_get_all_customers():
    request_helper = RequestUtility()
    response = request_helper.get('customers')
    assert response, f"Response for all customers cannot be empty"
