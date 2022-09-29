import pytest

from src.helpers.order_notes_helper import NotesHelper
from src.helpers.orders_helper import OrderHelper;
from src.utilities.genericUtilities import generate_random_string


@pytest.mark.tcid13
def test_create_order_note():
    order_helper = OrderHelper()
    NotesHelper
    # create an order
    new_order = order_helper.create_order()
    order_id = new_order['id']
    order_note = generate_random_string()
    response = NotesHelper().create_an_order_note(f'orders/{order_id}/notes', {'note': order_note})
    assert response, f"Create note response cannot be empty"
    # add a note
    # submit a note
    # confirm order is saved on db
