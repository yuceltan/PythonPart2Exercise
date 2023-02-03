class Animal:
    def __init__(self,run,leg_count):
        self.run=run
        self.leg_count=leg_count
        print("Animal object was created")
    def runs(self):
        print("Runnig started")
animal = Animal(True,4)
animal.runs()


