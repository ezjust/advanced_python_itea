class Auto:
    _seats = 4
    _wheels = 4
    _engine = "V8"
    _electro = False

    def get_seats(self):
        return self._seats

    def get_wheels(self):
        return self._wheels

    def get_electro(self):
        return self._electro

    def beep(self):
        print('BEEP')


class BUS(Auto):
    _seats = 40
    _wheels = 6

    def beep(self):
        print('Big BEEP')


class PassengerSmartCar(Auto):
    _seats = 2
    _electro = True
    _size = 'smallest'

    def beep(self):
        print("beep")

    def get_size(self):
        return self._size


passenger = PassengerSmartCar()
print(passenger.get_size())
print(passenger.get_wheels())
