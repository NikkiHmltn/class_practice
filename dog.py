class Dog():
    """This is a list of dogs I want"""
    def __init__(self, breed, size):
        self.breed = breed
        self.size = size
        self.pets = False
    
    def __str__(self):
        return "{},{}".format(self.breed, self.size)

    def pet(self):
        self.pets = True
        print("Woof woof!")

dog1 = Dog("Samoyed", "large")

dog1.pet()