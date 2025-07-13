import sqlite3
import functools
from with_db_connection import with_db_connection

def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
        raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cussor = conn.cursor()
    cursor.execute("UPDATE users SET email = ?WHERE id = ?", (new_email, user_id))

update_user_email(user_id=1, new_email='Crawford_Catwright@hotmail.com')