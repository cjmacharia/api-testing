from datetime import datetime, timedelta
import pytest

from src.dao.products_dao import ProductsDAO
from src.helpers.products_helper import ProductHelper


class TestListProductWithFilter:
    @pytest.mark.tcid07
    def test_list_product_with_filter_after(self):
        days_from_today = 30
        _after_created_time = datetime.now().replace(microsecond=0) - timedelta(days=days_from_today)
        after_created_time = _after_created_time.isoformat()
        payload = dict()
        payload['after'] = after_created_time
        payload['per_page'] = 100
        api_response = ProductHelper().call_list_products(payload)
        dp_product = ProductsDAO().get_product_created_after_a_date(after_created_time)
        id_in_api = [i['id'] for i in api_response]
        ids_in_db = [i['ID'] for i in dp_product]
        id_difference = list(set(ids_in_db) - set(id_in_api))
        assert api_response, f"empty response for list of products with filter"
        assert not id_difference, f"Products in db with 'after' filter do not match products returned bt the Api"
        assert len(dp_product) == len(api_response), f"List of product with filter 'after' returned an un expected " \
                                                     f"number of products." \
                                                     f"Expected: {len(dp_product)}, Actual: {len(api_response)}"

