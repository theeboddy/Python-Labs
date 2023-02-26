class Machine:
    def __init__(self, color, doors, wheel):
        self.color = color
        self.doors = doors
        self.wheel = wheel
    def drive(self):
        pass

class Car(Machine):
    def __init__(self, color, doors, wheel, model, __privod, type):
        Machine.__init__(self, color, doors, wheel)
        self.model = model
        self.privod = __privod
        self.type = type
    def drive(self):
        return f"Я вожу {self.color} {self.type} марки {self.model}"

class SpecialMachine(Machine):
    def __init__(self, color, doors, wheel, load_сapacity, type):
        Machine.__init__(self, color, doors, wheel)
        self.load_capacity = load_сapacity
        self.type = type
    def drive(self):
        return f"Под моим управлением находится {self.type} грузоподъемностью {self.load_capacity} тонн"

car1 = Car('чёрный', 3, 4, 'BMW', 'задний', 'Сидан')
car2 = SpecialMachine('жёлтый', 2, 6, 5, 'Грузовик')
print(car1.drive())
print(car2.drive())