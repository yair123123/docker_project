from sqlalchemy import Column, Integer,String
from config.base_user import BaseUser
class User(BaseUser):
    id = Column(Integer,primary_key = True,autoincrement=True)
    name = Column(String(100),nullable=False)