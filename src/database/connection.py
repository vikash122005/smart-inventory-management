import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="smart_inventory",
        user="postgres",
        password="root",
        port="5432"
    )
    return connection
