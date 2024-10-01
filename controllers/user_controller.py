from flask import Blueprint, jsonify
from reposiroty.user_repository import get_all

user_blueprint = Blueprint("user", __name__)

def to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@user_blueprint.route("/", methods=["GET"])
def get_all_users():
    users = get_all()  
    users_dict = [to_dict(user) for user in users]
    return jsonify(users_dict), 200
