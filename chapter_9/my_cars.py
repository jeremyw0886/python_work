from car import Car
import electric_car as ec

my_mustang = Car("ford", "mustang", 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ec.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
