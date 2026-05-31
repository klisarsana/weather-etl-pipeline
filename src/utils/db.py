import psycopg2
from psycopg2 import OperationalError
from config.settings import DB_CONFIG

def get_db_conn():
    """
    Membuat koneksi ke PostgreSQL
    Returns:
        connection object jika berhasil
        None jika gagal
    """
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            port=DB_CONFIG['port']
        )
        print('Database connection established')
        return conn
    except OperationalError as e:
        print(f'Database connection error: {e}')
        return None

def close_db_conn(conn):
    """
    Menutup koneksi database jika masih terbuka
    """
    if conn:
        conn.close()
        print('Database connection closed.')