from config.base_car import session_factory_car
from model.Car import Car


def get_all():
    with session_factory_car() as session:
        cars = session.query(Car).all() 
        return cars
def insert_car(car:Car):
    with session_factory_car() as session:
        session.add(car)
        session.commit()
        session.refresh(car)
        return car.id