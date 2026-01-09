from abc import ABC, abstractmethod

class Car:

    def __init__(self,options: list[str], size_tank: str, base_price: float):
        self._size_tank = size_tank
        self._base_price = base_price
        self._options = self.add_options(options)
    def get_options(self):
        return self._options

    def add_options(self,options):
        if len(options) <=3:
            return options
        else:
            print("Опций не может быть больше 3")
            return["Парктроник"]
    def calculate_price(self):
        return self._base_price + len(self._options)

    def __str__(self):
        return "Car"

class SmallTank(Car):
    def __init__(self, options, size="small", base_price=40):
         super().__init__(options, size, base_price)

class BigTank(Car):
    def __init__(self, options, size="big", base_price=70):
         super().__init__(options, size, base_price)

class Passengercar(SmallTank):
     def calculate_price(self):
         return (self._base_price + len(self._options)) * 500

     def __str__(self):
         return "Passengercar"

class Truck(Car):
     def calculate_price(self):
        return (self._base_price + len(self._options)) * 800

     def __str__(self):
        return "Truck"

class Order(ABC):
     @abstractmethod
     def buy(self):
         pass
class CarOrder(Order):

     def __init__(self, car: Car):
         self._car = car

     def  buy(self):
          print((f"Покупаем авто {self._car}: {self._car._size_tank}: Цена {self._car.calculate_price()}$"))

car = Passengercar(options=["Парктроник", "Гидроусилитель"])
order = CarOrder(car)
order.buy()

