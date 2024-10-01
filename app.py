from flask import Flask
from controllers.user_controller import user_blueprint
from controllers.car_controller import car_blueprint
from model.Car import Car
from model.User import User 
app = Flask(__name__)
@app.route("/")
def hello():
    return "hello"

app.register_blueprint(user_blueprint,url_prefix = "/api/users")
app.register_blueprint(car_blueprint,url_prefix = "/api/cars")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)