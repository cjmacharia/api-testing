import pymysql

from src.utilities.credentialsUtility import get_db_credentials


class DBUtility(object):
    def __init__(self):
        self.credentials = get_db_credentials()
        self.host = '127.0.0.1'

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.credentials['db_user'],
                                     password=self.credentials['db_password'], port=3306)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            details = cur.fetchall()
            return details
        except Exception as e:
            raise Exception(f"failed running :{sql} Error: {e}")
        finally:
            conn.close()
