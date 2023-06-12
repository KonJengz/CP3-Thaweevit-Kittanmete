class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAir(self):
        print("เปิด : แอร์")

class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

car1 = Car()
car1.turnOnAir()

pickUp1 = PickUp()
pickUp1.turnOnAir()

van1 = Van()
van1.turnOnAir()