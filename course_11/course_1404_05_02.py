from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def change_tire(self):
        pass

    @abstractmethod
    def start(self):
        pass


class Benz(Car):
    def change_tire(self):
        print("Change tire")

    def start(self):
        print("Start")


# c1 = Car()
b1 = Benz()
b1.change_tire()
b1.start()
print("hello world") 