from src.utilities.dbUtility import DBUtility
import random


class CustomersDAO:
    def __init__(self):
        self.db_utility = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM wordpress.wp_users WHERE user_email='{email}'"
        res_sql = self.db_utility.execute_select(sql)
        return res_sql

    def get_random_customer_from_db(self, qty=1):
        sql = "SELECT * FROM wordpress.wp_users"
        res_sql = self.db_utility.execute_select(sql)
        return random.sample(res_sql, qty)
