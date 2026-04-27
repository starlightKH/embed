import random
import math

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def make_point(self):
        self.x = random.randint(1, 20)
        self.y = random.randint(1, 20)

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        

    def show_point(self):
        print("좌표:", (self.x, self.y))
        print("원점까지 거리:", self.distance_from_origin())
        

p1 = Point()
p1.make_point()
p1.show_point()
p2 = Point()
p2.make_point()
p2.show_point()
print("두점사이의 거리:", p1.distance_to(p2))
