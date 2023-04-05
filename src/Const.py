# Shaid H00shi
from Vector import *
from Collision import *
from numpy import array
from scipy.integrate import quad
import Transform

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

    return square, abs(W - E)


def marab(square, rigid_body):
    Up_Left = square[0][0]
    Up_right = square[0][1]

    x = Up_Left.x
    y = Up_Left.y
    new_x = x
    new_y = y

    centers = [[], []]

    while x != Up_right.x:
        new_x = x + 0.1

        while y != Up_right.y:
            new_y = y + 0.1

        Square = [[Vector(x, y), Vector(new_x, y)], [Vector(new_x, y), Vector(new_x, new_y)], [
            Vector(new_x, new_y), Vector(x, new_y)], [Vector(x, new_y), Vector(x, y)]]

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


def calculate_inertia(rigid_body, a):
    square_vertices, x = find_square(rigid_body)
    square = Transform.Poly(square_vertices, rigid_body.mass, rigid_body.center)
    squares_mass = rigid_body.mass / (a * a)
    Inertia = 0 
    for x in range(rigid_body.sides[0][0].x,rigid_body.sides[0][0].x + a):
        for y in range(rigid_body.sides[0][0].y,rigid_body.sides[0][0].y + a):

            new_square_sides = [[Vector(x, y), Vector(x + 1, y)], [Vector(x + 1, y), Vector(x + 1, y + 1)], [
                Vector(x + 1, y + 1), Vector(x, y + 1)], [Vector(x, y + 1), Vector(x, y)]]
            new_square = Transform.Poly(new_square_sides, squares_mass, Vector(0,0))
            dx = new_square.center.x - rigid_body.center.x
            dy = new_square.center.y - rigid_body.center.y
            r = (dx**2 + dy**2)**0.5
            f = lambda g : r*r
            
            Inertia += 1 / 12 + r*r

    return Inertia
R1 = Transform.Poly([[Vector(100, 100), Vector(300,100)], [Vector(300, 100), Vector(300, 300)], [Vector(300, 300), Vector(100, 300)], [Vector(100, 300), Vector(100, 100)]], 30, Vector(100, 100))
# R1 = Transform.Poly([[Vector(0,0) , Vector(0,100)] , [Vector(0,100) , Vector(100,0)] , [Vector(100,0) , Vector(0,0)]], 100, Vector(0,0))
In = calculate_inertia(R1, 200) 
print(In/2)
print(200 ** 4 / 12)