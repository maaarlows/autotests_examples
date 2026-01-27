import pymysql

from db.db_pass import HOST, PORT, USER, PASSWORD, DATABASE


def fetch_one_mysql(query: str, params: tuple):
    conn = pymysql.connect(
        host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE,
        autocommit=True, cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchone()
    finally:
        conn.close()