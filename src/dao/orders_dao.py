from src.utilities.dbUtility import DBUtility


class OrdersDAO:
    def __init__(self):
        self.db_utility = DBUtility()

    def get_order_by_id(self, order_id):
        sql = f"SELECT * FROM wordpress.wp_woocommerce_order_items WHERE order_id='{order_id}'"
        res_sql = self.db_utility.execute_select(sql)
        return res_sql

    def get_order_item_meta(self, order_item_id):
        sql = f"SELECT * FROM wordpress.wp_woocommerce_order_itemmeta WHERE order_item_id='{order_item_id}'"
        res_sql = self.db_utility.execute_select(sql)
        line_details = dict()
        for meta in res_sql:
            line_details[meta["meta_key"]] = meta["meta_value"]
        return line_details
