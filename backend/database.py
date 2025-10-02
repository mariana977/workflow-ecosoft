import os
from dotenv import load_dotenv
from mysql.connector import pooling, MySQLConnection
import redis

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "admin123"),
    "database": os.getenv("MYSQL_DB", "dym_reciclaje"),
    "port": int(os.getenv("MYSQL_PORT", 3306))
}

pool = pooling.MySQLConnectionPool(pool_name="ecosoft_pool", pool_size=5, **DB_CONFIG)

def get_db_conn():
    return pool.get_connection()

# Redis client (synchronous) for simple caching
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
try:
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    redis_client.ping()
except Exception:
    redis_client = None