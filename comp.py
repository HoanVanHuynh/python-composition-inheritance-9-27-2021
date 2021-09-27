class Robot:
    def __init__(self, head, body, legs):
        self.head = head 
        self.body = body 
        self.legs = legs 

r = Robot('a head', 'a body', 2) 
print(r.body)