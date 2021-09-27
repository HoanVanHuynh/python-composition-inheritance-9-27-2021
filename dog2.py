class Animal():
    def eat(self):
        print('yum') 

class Dog(Animal):
    def bark(self):
        print('Woof!') 

class Cat(Animal):
    def meow(self):
        print('Meow') 


Snoopy = Dog() 
Garfield = Cat()
  
Snoopy.bark() 
Snoopy.eat()
Garfield.meow()
Garfield.eat()