from src.utilities.dbUtility import DBUtility
import random


class ProductsDAO:
    def __init__(self):
        self.db_utility = DBUtility()

    def get_random_products_from_db(self, qty=1):
        sql = f"SELECT * FROM wordpress.wp_posts WHERE post_type='product' LIMIT 100"
        res_sql = self.db_utility.execute_select(sql)
        return random.sample(res_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f"SELECT * FROM wordpress.wp_posts WHERE ID = {product_id}"
        return self.db_utility.execute_select(sql)

    def get_product_created_after_a_date(self, _date):
        sql = f"SELECT * FROM wordpress.wp_posts WHERE post_type='product' AND post_date > '{_date}'"
        return self.db_utility.execute_select(sql)


