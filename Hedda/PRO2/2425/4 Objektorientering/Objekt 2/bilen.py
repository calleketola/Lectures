class Car():

    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        self.speed = 0

    def drive(self):
        print(self.brand + f": Kör {self.speed} km/h framåt")

    def honk(self):
        print(self.brand + ": Tut tut!")

    def breaking(self):
        self.speed = 0
        print(self.brand+ ": Bromsar...")

    def accelerate(self, a):
        self.speed += a
        

bil1 = Car("Volvo", 2018, "Vit")

bil1.drive()
bil1.accelerate(50)
bil1.drive()
bil1.accelerate(5)
bil1.drive()
bil1.breaking()
bil1.drive()
