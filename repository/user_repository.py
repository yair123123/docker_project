from config.base_user import session_factory_user
from model.User import User
from sqlalchemy.exc import SQLAlchemyError


def get_all():
    with session_factory_user() as session:
        users = session.query(User).all()
        return users
def insert_user(user:User):
    with session_factory_user() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user.id
        except SQLAlchemyError as e:
            session.rollback()
            return str(e)