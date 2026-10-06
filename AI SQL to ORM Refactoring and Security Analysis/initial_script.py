import mysql.connector
from mysql.connector import Error


def get_connection():
    """Establish and return a database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="example_db"
    )


def create_user(db_cursor, username, email):
    """Create a new user safely using parameterized queries."""
    if not username or not email:
        print("Username and email are required.")
        return
    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    try:
        db_cursor.execute(sql, (username, email))
        print(f"User '{username}' created successfully.")
    except Error as e:
        print(f"Error creating user: {e}")


# The remaining functions are get_user_by_username, update_user_email,
# delete_user and list_users, each following the same parameterized style.
# (They were truncated in the assignment text, so they are not included.)
