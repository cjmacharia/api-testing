import logging

from src.utilities.genericUtilities import generate_random_email_and_password
from src.utilities.requestUtility import RequestUtility


class ProductHelper(object):
    def __init__(self):
        self.request_utility = RequestUtility()

    def get_products_by_id(self, product_id):
        return self.request_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.request_utility.post("products", payload=payload, expected_status_code=201)

    def call_list_products(self, payload):
        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logging.debug(f"List product page: {i}")
            payload['per_page'] = 100

            # add page number to the call
            payload['page'] = i
            response = self.request_utility.get('products', payload=payload)
            if not response:
                break
            else:
                all_products.extend(response)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages")
        return all_products

