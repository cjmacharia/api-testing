import os


def get_wc_api_keys():
    wc_key = os.getenv('WC_KEY')
    wc_secret = os.getenv('WC_SECRET')

    if not wc_key or not wc_secret:
        raise Exception("The api credentials are not in the .env")
    else:
        return {'wc_key': wc_key, 'wc_secret': wc_secret}


def get_db_credentials():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')
    return {'db_user': db_user, 'db_password': db_password, 'db_port': db_port}


class CredentialsUtility(object):
    pass
