from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection parameters for the first database
DB1_NAME = "database1"
DB1_USER = "car"
DB1_PASS = "1234"
DB1_HOST = "my-postgres1"  
DB1_PORT = "5432"        

engine_db1 = create_engine(f'postgresql://{DB1_USER}:{DB1_PASS}@{DB1_HOST}:{DB1_PORT}/{DB1_NAME}')

_session_factory_db1 = sessionmaker(bind=engine_db1)


BaseCar = declarative_base()

def session_factory_car():
    BaseCar.metadata.create_all(engine_db1)  # יצירת הטבלאות אם אין
    return _session_factory_db1()


