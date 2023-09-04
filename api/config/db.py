from sqlalchemy import create_engine, MetaData

db_url = "postgresql://postgres:admin@localhost:5432/database_python_fast_api"
engine = create_engine(db_url)

meta = MetaData()

conn = engine.connect()

