class Dog():
    def bark(self):
        print('Woof!') 

class Robot():
    def move(self):
        print('ahh..mobility')

class CleanRobot():
    def clean(self):
        print('I vacuum dust') 

class SuperRobot():
    def __init__(self):
        #'this class contains 3 objects'
        self.o1 = Robot() 
        self.o2 = Dog() 
        self.o3 = CleanRobot() 
    
    def playGame(self):
        print('chess is best!') 
    
    def move(self):
        return self.o1.move() 
    
    def bark(self):
        return self.o2.bark() 
    
    def clean(self):
        return self.o3.clean() 

henry = SuperRobot() 
henry.move()