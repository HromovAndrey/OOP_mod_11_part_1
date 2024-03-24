
class Dogs:
    def __int__(self, name, age, bread):
        self.name = name
        self.age = age
        self.bread = bread
    pass
#створення  екземпляру класу
my_dogs = Dogs("Бобік", 3, "Лабродор" )
print(my_dogs.name)
print(my_dogs.age)

#Завдання 1
#Створіть клас Student з атрибутами name та age.
#Додайте метод print_info, який виведе інформацію про
#студента у на вигляді "Ім'я: {name}, Вік: {age}".

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def  print_info(self):
        print(f"Імя студента та {self.name}його вік{self.age}")
student1 = Student("Іван", 20)
student1.print_info()
