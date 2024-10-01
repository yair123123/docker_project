from config.base_user import session_factory_user
from model import User


def get_all():
    with session_factory_user() as session:
        users = session.get(User,all)
        return users