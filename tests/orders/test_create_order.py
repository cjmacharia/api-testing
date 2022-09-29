import pytest

from src.dao.products_dao import ProductsDAO
from src.helpers.customers_helper import CustomerHelper

from src.helpers.orders_helper import OrderHelper


@pytest.fixture(scope="module")
def orders_set_up():
    product_dao = ProductsDAO()
    random_product = product_dao.get_random_products_from_db(1)
    product_id = random_product[0]['ID']
    order_helper = OrderHelper()
    info = {'product_id': product_id, 'order_helper': order_helper}
    return info


@pytest.mark.tcid08
def test_create_paid_order_guest_user(orders_set_up):
    # get product from db
    customer_id = 0
    product_id = orders_set_up['product_id']
    order_helper = orders_set_up['order_helper']
    # make a call
    data = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 2
        },

    ]}
    order = order_helper.create_order(additional_argument=data)
    expected_product = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order, customer_id, expected_product)


@pytest.mark.tcid09
def test_create_new_order_new_customer(orders_set_up):
    # helper objects
    order_helper = orders_set_up['order_helper']
    product_id = orders_set_up['product_id']

    customer_helper = CustomerHelper()
    # get product from db

    customer_info = customer_helper.create_customer()
    customer_id = customer_info['id']
    # make a call
    data = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 2
        },
    ],
        "customer_id": customer_id
    }
    expected_product = [{'product_id': product_id}]
    order = order_helper.create_order(additional_argument=data)
    order_helper.verify_order_is_created(order, customer_id, expected_product)
