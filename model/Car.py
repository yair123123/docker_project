from sqlalchemy import Column, Integer,String
from config.base_car import Base
class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer,primary_key = True,autoincrement=True)
    color = Column(String(100),nullable=False)