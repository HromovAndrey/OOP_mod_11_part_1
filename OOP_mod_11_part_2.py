class Animals:
    def breathe(self):
        print("дихає")
    def move(self):
        print("рухається")
    def eat_food(self):
        print("їсть")
class Dogs(Animals):
    pass
class Cats(Animals):
    pass
#Створення екзепляру класу
my_dog = Dogs()
#мотоди
my_dog.breathe()
my_dog.move()
