class Animals:
    def breath(self):
        print("дихає")

    def move(self):
        print("рухається")

    def eat_food(self):
        print("Їсть")

class Dogs(Animals):
    pass
class Cats(Animals):
    pass
#Сворення екземпляру класу
my_dog = Dog()
my_dog.dreath()