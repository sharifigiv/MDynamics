# Shaid H00shi

from Vector import *
def find_square(rigid_body):
    N = 0
    W = 0
    E = 0
    S = 0
    for line in rigid_body.sides:
        for point in line:
            if point.y >= N:
                N = point.y
            elif point.y <= S:
                S = point.y
            if point.x <= W:
                W = point.x
            elif point.x >= E:
                E = point.x
    square = [[Vector(N, W), Vector(N, E)], [Vector(N, E), Vector(S, E)], [Vector(S, E), Vector(S, W)], [Vector(S, W), Vector(N, W)]]
    return square
class Square:
    def __init__(self):
        self.sides = [[Vector(0, 0), Vector(1, 0)], [Vector(1, 0), Vector(1, 1)], [Vector(1,1), Vector(0,1)], [Vector(0,1) , Vector(0,0)]]
x = Square()
for i in find_square(x):
    for p in i:
        print("================================")
        print(p.x)
        print(p.y)