import pytest

from src.helpers.orders_helper import OrderHelper


@pytest.mark.regression
@pytest.mark.parametrize("new_status",
                         [
                             pytest.param('completed', marks=pytest.mark.tcid11),
                             pytest.param('on-hold', marks=pytest.mark.tcid12),
                             pytest.param('cancelled', marks=pytest.mark.tcid13),
                         ])
def test_update_order_status(new_status):
    # create new order
    order_helper = OrderHelper()
    order = order_helper.create_order()
    cur_status = order['status']

    assert cur_status != new_status, f"Current status is already {new_status}"

    # update status
    order_id = order['id']
    payload = {"status": new_status}
    order_helper.call_update_order(order_id, payload)

    # get other info
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    # verify
    assert new_order_info['status'] == new_status, f"Update order status to '{new_status}, " \
                                                   f"but order is still {new_order_info['status']}"


@pytest.mark.tcid15
def test_update_an_invalid_status():
    new_status = 'invalid'
    order_helper = OrderHelper()
    order = order_helper.create_order()

    # update status
    order_id = order['id']
    payload = {"status": new_status}
    api_response = order_helper.call_update_order(order_id, payload, expected_status_code=400)
    assert api_response['code'] == 'rest_invalid_param', f"Update invalid order status did not have correct code in " \
                                                         f"response" \
                                                         f"Expected:'rest_invalid_param' Actual: {api_response['code']}"
    assert api_response[
               'message'] == 'Invalid parameter(s): status', f"Update invalid order status did not have message" \
                                                             f" in response " \
                                                             f"Expected: 'Invalid parameter(s): status' " \
                                                             f"Actual: {api_response['message']}"
