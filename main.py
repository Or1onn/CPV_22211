class Person:
    def eat(self):
        print("Eat")


class Student(Person):
    def __init__(self):
        self.name = "Ziya"
        self.age = 14
        self.height = 172
        self.school = 23

    def Eat(self):
        super().eat()

    def AboutMe(self):
        print("My name is " + self.name)
        print("My age is " + self.age.__str__())
        print("My height is " + self.height.__str__())


def nextSquare():
    i = 1

    while True:
        yield i * i
        i += 1


for num in nextSquare():
    if num > 100:
        break
    print(num)