import math 
class Distance_two_pointer:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def distance(self):  
        return math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)

dis = Distance_two_pointer(4, 0, 6, 6)
print(dis.distance())