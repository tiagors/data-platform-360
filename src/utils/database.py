import psycopg

def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="data_platform",
        user="data_engineer",
        password="data123"
    )