class Dog:
    def __init__(self,age,name):
        self.name = name
        self.age = age

    def make_bark(self):
        return "Woof"
    def meth_eat(self):
        return "eating"    
    def food_type(self,type,leather):
        self.type = type
        self.leather = leather
        return self.type,self.leather


phase2 = Dog(21,"Tom")

print(phase2.food_type("bones","fur"))

