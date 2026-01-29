import time

from db.db_conn import fetch_one_mysql


def is_user_pro(email:str) -> bool:
    row = fetch_one_mysql(
        """
                SELECT subscribe_till
                FROM users
                WHERE email = %s
                """,
        (email,)
    )
    return row["subscribe_till"] is not None

def wait_until_user_is_pro(email, timeout=60, step=2):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if is_user_pro(email):
            return
        time.sleep(step)
    raise AssertionError(f"User {email} was not upgraded to PRO within {timeout} seconds")

def check_new_sim(first_name, last_name):
    row = fetch_one_mysql(
        """
                SELECT *
                FROM person
                WHERE first_name = %s AND last_name = %s
                LIMIT 1
                """,
        (first_name, last_name)
    )
    return row is not None
