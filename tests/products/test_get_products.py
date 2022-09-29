import logging

import pytest

from src.dao.products_dao import ProductsDAO
from src.helpers.products_helper import ProductHelper
from src.utilities.requestUtility import RequestUtility


@pytest.mark.tcid04
def test_get_all_products():
    request_helper = RequestUtility()
    response = request_helper.get('products')
    assert response, f"Response for all products cannot be empty"


@pytest.mark.tcid05
def test_get_product_by_id():
    # get a product from the db

    random_product = ProductsDAO().get_random_products_from_db(1)
    random_product_id = random_product[0]['ID']
    prod_helper = ProductHelper()
    response = prod_helper.get_products_by_id(random_product_id)
    # compare name returned by db vs the api name
    assert random_product[0]['post_title'] == response['name'], f"Product by id returned wrong product" \
                                                                f"id: {random_product_id} " \
                                                                f"DB name:{random_product[0]['post_title']}" \
                                                                f"API name: {response['name']}"
