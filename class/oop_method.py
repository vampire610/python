class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hi, my name is :', self.name)


p = Person('asd')

p.say_hi()
