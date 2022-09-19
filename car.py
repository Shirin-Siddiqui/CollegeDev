class Car():
    def __init__(self, year, mpg, speed, list_of_owners):
        self.year = year
        self.mpg = mpg
        self.speed = speed
        self.list_of_owners = list_of_owners
    
    def accelerate(self):
        self.speed = self.speed + 30
        return (f"The speed is increased by 30: {self.speed} km/hr")
        
    def brake(self):
        self.speed = self.speed - 60
        return (f"The speed is decreased by 60: {self.speed} km/hr" )
            
    def owners(self):
        return (f"The complete list of owners if this car is {self.list_of_owners}")
    
    def __str__(self):
        return (f"The complete info of this car is: MANUFACTURING YEAR: {self.year} MILES : {self.mpg} SPEED: {self.speed} km/hr")

car1 = Car(2016,60,100,['Shirin', 'Shivangi'])

print(car1.accelerate())
print(car1.accelerate())
print(car1.brake())



