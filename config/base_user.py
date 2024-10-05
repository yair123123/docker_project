from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine


DB2_NAME = "users"
DB2_USER = "postgres"
DB2_PASS = "1234"
DB2_HOST = "users"
DB2_PORT = "5432"

engine_db = create_engine(f'postgresql://{DB2_USER}:{DB2_PASS}@{DB2_HOST}:{DB2_PORT}/{DB2_NAME}')
_session_factory = sessionmaker(bind=engine_db)
Base = declarative_base()
def session_factory_user():
    Base.metadata.create_all(engine_db)
    return _session_factory()