import psycopg2.pool

# Create a connection pool with a maximum of 10 connections
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host="localhost",
    port="5432",
    database="files",
    user="myuser",
    password="mypassword"
)

def get_db_conn():
    conn = connection_pool.getconn()
    return conn

def release_db_conn(conn):
    connection_pool.putconn(conn)