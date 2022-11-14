# Name: Jacob Newby
# Date: 11/14/2022
# Desription: To show functionality of classes and funtions. We do this by creating a class called
#   called vehicles and a subclass called automobile.

# New Vehicle Class
class Vehicle:
    def __init__(self,type):
        self.type=type

#New Automobile Subclass
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        # Used to invoke vehicle class constructor
        super().__init__(type)
        self.year=year
        self.make=make
        self.model=model
        self.doors=doors
        self.roof=roof

# Have user input information
type_i=input("Type of vehicle: ")
year_i=input("Enter the year: ")
make_i=input("Enter the make: ")
model_i=input("Enter the model: ")
doors_i=input("Enter the number of doors: ")
roof_i=input("Enter solor or sun roof: ")
# Call contructor with all values read
A=Automobile(type_i, year_i, make_i, model_i, doors_i, roof_i)

#Print out the output
print("\nVehicle Type: "+A.type)
print("\nYear: "+A.year)
print("\nMake: "+A.make)
print("\nModel: "+A.model)
print("\nNumber of doors: "+A.doors)
print("\nType of roof: "+A.roof)