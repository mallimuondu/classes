class Vehicle:
    def __init__(self,name,capasity,milage):
        self.name = name
        self.capasity = capasity
        self.milage = milage
    def fare(self):
        return self.capasity * 100
    
class Bus(Vehicle):
    def fare(self):
        ammount = super().fare()
        ammount += ammount * 10/100
        return ammount
#        Vehicle.__init__(self,name,capasity,milage)
        
bus1 = Bus('schoolbus',50,100000)
print('total bus fare is ',bus1.fare())