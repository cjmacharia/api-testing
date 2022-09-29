import pytest
from src.dao.products_dao import ProductsDAO
from src.helpers.products_helper import ProductHelper
from src.utilities.genericUtilities import generate_random_string


@pytest.mark.tcid06
def test_create_product():
    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(15)
    payload['type'] = "simple"
    payload['regular_price'] = '10.19'

    # make call
    response = ProductHelper().call_create_product(payload)
    # assert response is not empty
    assert response, f"Create product api response is empty"
    assert response['name'] == payload['name'], f"Created product has an unexpected name " \
                                                f"expected {payload['name']}, Actual{response['name']}"
    # verify product exists in db
    product_id = response['id']
    db_product = ProductsDAO().get_product_by_id(product_id)
    assert payload['name'] == db_product[0]['post_title'], f"Created product title does not match the db title" \
                                                           f"Expected: {payload['name']}" \
                                                           f"Actual: {db_product['post_title']}"
