import pytest
from ipynb.fs.full.index import Driver, Passenger

def test_driver_instance_methods_decorators():
    new_driver = Driver()
    new_driver.first = "Ron"
    new_driver.last = "Burgundy"
    new_driver.miles_driven = 20
    new_driver.rating = 3.0
    assert new_driver._first == "Ron"
    assert new_driver.first == "Ron"
    assert new_driver._last == "Burgundy"
    assert new_driver.last == "Burgundy"
    assert new_driver._miles_driven == 20
    assert new_driver.miles_driven == 20
    assert new_driver._rating == 3.0
    assert new_driver.rating == 3.0
    assert new_driver.greet_passenger() == "Hello! I'll be your driver today. My name is Ron Burgundy"

def test_passenger_instance_methods_decorators():
    new_passenger = Passenger()
    new_passenger.first = "Melissa"
    new_passenger.last = "Morris"
    new_passenger.email = "melissa.morris@gmail.com"
    assert new_passenger._first == "Melissa"
    assert new_passenger.first == "Melissa"
    assert new_passenger._last == "Morris"
    assert new_passenger.last == "Morris"
    assert new_passenger._email == "melissa.morris@gmail.com"
    assert new_passenger.email == "melissa.morris@gmail.com"
    assert new_passenger.yell_name() == "MELISSA MORRIS"
