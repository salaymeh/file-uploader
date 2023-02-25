import psycopg2
# Define a function to create a connection to the PostgreSQL database

def get_db_conn():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="files",
        user="myuser",
        password="mypassword"
    )
    return conn
