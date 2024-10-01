from flask import Blueprint, jsonify, request
from model.User import User
from repository.user_repository import get_all, insert_user

user_blueprint = Blueprint("users", __name__)

def to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@user_blueprint.route("/", methods=["GET"])
def get_all_users():
    users = get_all()  
    users_dict = [to_dict(user) for user in users]
    return jsonify(users_dict), 200

@user_blueprint.route("/create",methods=["POST"])
def post_user():
    user_as_json = request.json
    user = User(name = user_as_json["name"])
    return jsonify(insert_user(user)),200