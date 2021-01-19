class Car:
    name = "BMW"
    _price = 20
    ___color = "Red"


class CarType(Car):
    def __init__(self):
        model = "Band"
        print("The price is {:d} and the color is {}".format(
            self._price, self._Car___color))


car_type = CarType()
