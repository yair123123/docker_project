from sqlalchemy import Column, Integer,String
from config.base_user import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,autoincrement=True)
    name = Column(String(100),nullable=False)
