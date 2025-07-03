# db_connect.py

import psycopg2

def get_connection():
    """
    Returns a connection and cursor to the PostgreSQL database.
    Change the DB credentials as needed.
    """
    DB_NAME = "remoteok"
    DB_USER = "postgres"
    DB_PASSWORD = "admin123"
    DB_HOST = "localhost"
    DB_PORT = "5432"

    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        return conn, cursor
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        raise
