from src.utilities.requestUtility import RequestUtility


class NotesHelper:

    def __init__(self):
        self.request_utility = RequestUtility()

    def create_an_order_note(self, endpoint, payload):
        return self.request_utility.post(endpoint=endpoint, payload=payload, expected_status_code=201)
