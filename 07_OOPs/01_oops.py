# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " ! "

    def fullname(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,__brand,model,battery_size):
        super().__init__(__brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.model)
print(my_tesla.fullname())
# print(my_tesla.__brand)
print(my_tesla.get_brand())


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullname())

# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_car.fullname())

