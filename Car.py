from abc import ABC, abstractmethod 

class Car(ABC) : 
    @abstractmethod
    def __init__(self, car_name, model, year) :
        self.car_name = car_name
        self.model = model
        self.year = year
    
    @abstractmethod
    def display_info(self) : 
        print("Car Information: ")
        print(f"\t{self.year} {self.car_name} {self.model}")

class ElectricCar(Car) : 
    def __init__(self, car_name, model, year, battery_capacity):
        super().__init__(car_name, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"\tBattery Capacity: {self.battery_capacity} kWh")

class GasCar(Car) : 
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency

    def display_info(self):
        super().display_info()
        print(f"\tFuel Efficiency: {self.fuel_efficiency} MPG")

class CarFactory:
    def get_car(self, car_type, car_name, model, year):
        if car_type == 'Electric':
            battery_capacity = input("Enter battery capacity (kWh): ")
            return ElectricCar(car_name, model, year, battery_capacity)
        elif car_type == 'Gas':
            fuel_efficiency = input("Enter fuel efficiency (MPG): ")
            return GasCar(car_name, model, year, fuel_efficiency)

def Car_Client():
    while True:
        car_type = input('Enter car type (Electric/Gas): ')
        if car_type !='Electric' and car_type !='Gas' :
            print('Not Available.')
            break

        car_name = input("Enter Name: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        
        Car_Factory = CarFactory()
        Car_Instance = Car_Factory.get_car(car_type, car_name, model, year)

        if Car_Instance:
            Car_Instance.display_info()

if __name__ == '__main__':
    Car_Client()