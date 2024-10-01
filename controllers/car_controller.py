from flask import Blueprint, jsonify, request
from model.Car import Car
from repository.car_repository import get_all , insert_car

car_blueprint = Blueprint("cars", __name__)

def to_dict(obj):
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

@car_blueprint.route("/", methods=["GET"])
def get_all_users():
    cars = get_all()  
    cars_dict = [to_dict(user) for user in cars]
    return jsonify(cars_dict), 200
@car_blueprint.route("/create",methods=["POST"])
def post_user():
    car_as_json = request.json
    car = Car(name = car_as_json["color"])
    return insert_car(car)