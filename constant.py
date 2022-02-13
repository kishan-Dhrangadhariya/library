SECRET_KEY = "MY_SECRET_KEY!!"
DB_URI = "postgresql://postgres:my_db_password@localhost:5432/library"
DB_CONN_POOL = 5
SQLALCHEMY_ENGINE_MOD = {
    "pool_pre_ping": True,
    "pool_recycle": 300
}
