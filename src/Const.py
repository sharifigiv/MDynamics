# Shaid H00shi

from Vector import *
from Collision import *
from Transform import *
from numpy import array

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

    square = [[Vector(W, N), Vector(E, N)], [Vector(E, N), Vector(E, S)], [
        Vector(E, S), Vector(W, S)], [Vector(W, S), Vector(W, N)]]

    return square

def marab(square, rigid_body):
    Up_Left = square[0][0]
    Up_right = square[0][1]

    x = Up_Left.x ; y = Up_Left.y
    new_x = x; new_y = y

    centers = [[], []]

    while x != Up_right.x:
        new_x = x + 0.1

        while y != Up_right.y:
            new_y = y + 0.1

        Square = [[Vector(x, y) , Vector(new_x, y)], [Vector(new_x, y), Vector(new_x, new_y)], [Vector(new_x, new_y), Vector(x, new_y)], [Vector(x, new_y), Vector(x, y)]]

        x += 0.1
        y += 0.1

        sumx = 0
        sumy = 0
        points = []
        for side in Square:
            if side[0] not in points:
                sumx += side[0].x

                sumy += side[0].y
                points.append(side[0])

            if side[1] not in points:
                sumx += side[1].x
                sumy += side[1].y
                points.append(side[1])

        center = Vector(sumx/len(points), sumy/len(points))
        centers[0].append(center.x)
        centers[1].append(center.y)
        

    centerss = array(centers)
    center_m = array([[rigid_body.x], [rigid_body.y]])

    ones = [1] * len(centers)
    ones = array(ones)    

# R1 = Poly([[Vector(100, 100), Vector(200,100)], [Vector(200, 100), Vector(200, 200)], [Vector(200, 200), Vector(100, 200)], [Vector(100, 200), Vector(100, 100)]], 30, Vector(100, 100))
# ss = find_square(R1)
# In = marab(ss, R1)
# print(In)
# print(30 * 100 * 100)

a = array([[1], [2]])
print(a)