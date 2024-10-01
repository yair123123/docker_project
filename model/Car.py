from sqlalchemy import Column, Integer,String
from config.base_car import BaseCar
class User(BaseCar):
    id = Column(Integer,primary_key = True,autoincrement=True)
    color = Column(String(100),nullable=False)