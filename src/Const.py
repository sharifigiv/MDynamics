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
    line = W - E
    
    return square, line


def calculate_inertia(rigid_body, a):
    square_vertices, x = find_square(rigid_body)
    square = Transform.Classic_Poly(square_vertices, rigid_body.mass, rigid_body.center)
    squares_mass = rigid_body.mass / (a * a)
    Inertia = 0 
    
    for x in range(rigid_body.sides[0][0].x,rigid_body.sides[0][0].x + a):
        for y in range(rigid_body.sides[0][0].y,rigid_body.sides[0][0].y + a):

            new_square_sides = [[Vector(x, y), Vector(x + 1, y)], [Vector(x + 1, y), Vector(x + 1, y + 1)], [
                Vector(x + 1, y + 1), Vector(x, y + 1)], [Vector(x, y + 1), Vector(x, y)]]
            new_square = Transform.Classic_Poly(new_square_sides, squares_mass, Vector(0,0))
            
            dx = new_square.center.x - rigid_body.center.x
            dy = new_square.center.y - rigid_body.center.y
            
            r = (dx ** 2 + dy ** 2)**0.5
            
            if dx > 0:
                if dy > 0:
                    r = ((dx-0.5) ** 2 + (dy+0.5) ** 2)**0.5
                # else:
                #     r = ((dx-0.5) ** 2 + (dy-0.5) ** 2)**0.5
            else:
                if dy > 0:
                    r = ((dx+0.5) ** 2 + (dy+0.5) ** 2)**0.5
                    
            Inertia += 1 / 12 + r*r
            
    return Inertia
