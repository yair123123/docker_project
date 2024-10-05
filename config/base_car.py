from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

DB1_NAME = "cars"
DB1_USER = "postgres"
DB1_PASS = "1234"
DB1_HOST = "cars"  
DB1_PORT = "5432"        

engine_db = create_engine(f'postgresql://{DB1_USER}:{DB1_PASS}@{DB1_HOST}:{DB1_PORT}/{DB1_NAME}')

_session_factory = sessionmaker(bind=engine_db)
Base = declarative_base()
def session_factory_car():
    Base.metadata.create_all(engine_db)
    return _session_factory()