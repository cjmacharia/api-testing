import json
import os.path

from src.utilities.wooApiUtility import WooApiUtility
from src.dao.orders_dao import OrdersDAO


class OrderHelper:
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooApiUtility()

    def create_order(self, additional_argument=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template) as data:
            payload = json.load(data)

        # if user has additional_argument then update it
        if additional_argument:
            assert isinstance(additional_argument, dict), f"Additional args must be a dictionary {additional_argument}"
            payload.update(additional_argument)
        return self.woo_helper.post('orders', data=payload, expected_status_code=201)

    def verify_order_is_created(self, order, customer_id, exp_product):
        # verify response
        order_dao = OrdersDAO()
        assert order, f"Order response can not be empty"
        assert order['customer_id'] == customer_id, f"Create customer id is not the correct customer id" \
                                                    f" Expected: {customer_id}, Actual: {order['customer_id']}"
        assert len(order['line_items']) == len(exp_product), f"Expected only {len(exp_product)} item in `line_items` " \
                                                             f"but got " \
                                                             f"{len(order['line_items'])}"

        # validate db
        order_info = order_dao.get_order_by_id(order['id'])
        line_items = [i for i in order_info if i['order_item_type'] == 'line_item']
        assert order_info, f"order info not found in db Order id: {order['id']}"
        assert len(line_items) == 1, f"Expected only one item in `line_items` but got " \
                                     f"{line_items}"

        # get list of product ids in teh response
        api_product_ids = [i['product_id'] for i in order['line_items']]
        for product in exp_product:
            assert product['product_id'] in api_product_ids, f"Create order does not have at least 1 " \
                                                             f"expected product in db"

    def call_update_order(self, order_id, payload, expected_status_code=200):
        return self.woo_helper.put(f'orders/{order_id}', payload, expected_status_code)

    def call_retrieve_an_order(self, order_id):
        return self.woo_helper.get(f'orders/{order_id}')
