class Head:
    def __init__(self, type):
        self.type = type 
    
    def get_type(self):
        return self.type 

class Body:
    def __init__(self, size):
        self.type = size 
    # def __repr__(self):
    #     return "This is a: {}".format(self.type)
    def get_size(self):
        return self.type  
class Leg:
    def __init__(self, number):
        self.number = number  
    def get_number(self):
        return self.number 

class Robot:
    def __init__(self, head, body, legs):
        if isinstance(head, Head):
            print('valid param')
        self.head = head 
        self.body = body 
        self.legs = legs 

head = Head('metal spikes') 
body = Body("S meters") 
leg = Leg(4)
my_robot = Robot(head,body,leg) 

print(my_robot)
print(my_robot.body)
my_robot.body.get_size()
print(my_robot.body.get_size())