from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB2_NAME = "database2"
DB2_USER = "user"
DB2_PASS = "1234"
DB2_HOST = "my-postgres2"
DB2_PORT = "5432"
engine_db2 = create_engine(f'postgresql://{DB2_USER}:{DB2_PASS}@{DB2_HOST}:{DB2_PORT}/{DB2_NAME}')
_session_factory_db2 = sessionmaker(bind=engine_db2)

BaseUser = declarative_base()

def session_factory_user():
    BaseUser.metadata.create_all(engine_db2)
    return _session_factory_db2()