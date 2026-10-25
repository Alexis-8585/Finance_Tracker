import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv  

load_dotenv()  # Load environment variables from .env file


### Functions ###
def setup_database():
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """
        )


def get_conn():
    return psycopg.connect(os.environ["DATABASE_URL"], row_factory=dict_row)

def get_user(username: str):
    with get_conn() as conn:
        return conn.execute(
            "SELECT username, password FROM users WHERE username = %s", (username,)
        ).fetchone()

def create_user(username: str, password: str):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )