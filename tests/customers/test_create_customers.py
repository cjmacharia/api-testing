import pytest
import logging as logger

from src.dao.customers_dao import CustomersDAO
from src.helpers.customers_helper import CustomerHelper
from src.utilities.genericUtilities import generate_random_email_and_password
from src.utilities.requestUtility import RequestUtility


@pytest.mark.tcid01
def test_create_customer_only_email_password():
    info = generate_random_email_and_password()
    email = info['email']
    password = info['password']
    # make the call
    customer_obj = CustomerHelper()
    cust_api_info = customer_obj.create_customer(email=email, password=password)

    assert cust_api_info['email'] == email, f"Create customer api return wrong email: {email}"
    cust_dao = CustomersDAO()
    customer_db_info = cust_dao.get_customer_by_email(email)
    # verify email in response

    # verify customer is created in database
    id_in_api = cust_api_info['id']
    id_in_db = customer_db_info[0]['ID']
    assert id_in_db == id_in_api, f"Create customer id not same as 'ID' in database" \
                                  f'Email: {email}'


@pytest.mark.tcid03
def test_create_customer_fail_for_existing_email():
    # Get customer email from database
    cust_dao = CustomersDAO()
    existing_customer = cust_dao.get_random_customer_from_db(qty=1)
    existing_email = existing_customer[0]['user_email']
    request_helper = RequestUtility()
    payload = {"email": existing_email, "password": "password"}
    response = request_helper.post(endpoint="customers", payload=payload, expected_status_code=400)
    assert response['code'] == "registration-error-email-exists", f"Create existing user error 'code' is incorrect." \
                                                                  f"Expected :registration-error-email-exists " \
                                                                  f"Actual: {response['code']}"


