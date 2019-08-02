from abc import ABC, abstractmethod


class BasicCar(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(BasicCar):

    def move(self):
        super().move()

    def stop(self):
        super().move()
        print('Stop')


a = Car()
a.stop()




