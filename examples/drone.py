import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as vec
import src.Spring as Spring
import src.Body as MDynamics
import src.Collision as collision
import pyray as pr 

phy = MDynamics.MDynamics(1080, 720)
pr.init_window(1080, 720, "Drone 2D")

Motor1 = phy.poly_rigidBody("Motor1", 500, 300, 10, [[vec.Vector(500, 300), vec.Vector(525, 300)], [vec.Vector(525, 300), vec.Vector(525, 350)], [vec.Vector(525, 350), vec.Vector(500, 350)], [vec.Vector(500, 350), vec.Vector(500, 300)]])
Motor2 = phy.poly_rigidBody("Motor1", 600, 300, 10, [[vec.Vector(600, 300), vec.Vector(625, 300)], [vec.Vector(625, 300), vec.Vector(625, 350)], [vec.Vector(625, 350), vec.Vector(600, 350)], [vec.Vector(600, 350), vec.Vector(600, 300)]])

speeding_motor = False

def rotate_motor(Motor, angle):
    for line in Motor.sides:
        for point in line:
            point2 = vec.rotate(Motor.center, point, angle)
            line[line.index(point)] = point2

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    if pr.is_key_down(263):
        rotate_motor(Motor1, 0.05)
        rotate_motor(Motor2, 0.05)

    if pr.is_key_down(262):
        rotate_motor(Motor1, -0.05)
        rotate_motor(Motor2, -0.05)

    if pr.is_key_down(32):
        speeding_motor = True

        vector1 = Motor1.sides[1][1] - Motor1.sides[1][0]
        vector2 = Motor2.sides[1][1] - Motor2.sides[1][0]

        Motor1.acceleration += vec.Vector(-vector1.x // 2, -vector1.y // 2)
        Motor2.acceleration += vec.Vector(-vector2.x // 2, -vector2.y // 2)

    if pr.is_key_released(32):
        if speeding_motor:
            speeding_motor = False
            Motor1.velocity = vec.Vector(0, 0)
            Motor2.velocity = vec.Vector(0, 0)

    Motor1.acceleration += vec.Vector(0, 9)
    Motor2.acceleration += vec.Vector(0, 9)

    Motor1.update(0.003, 1080, 720, edges = False)
    Motor2.update(0.003, 1080, 720, edges = False)

    for line in Motor1.sides:
        pr.draw_line(int(line[0].x), int(line[0].y), int(
            line[1].x), int(line[1].y), pr.WHITE)

    for line in Motor2.sides:
        pr.draw_line(int(line[0].x), int(line[0].y), int(
            line[1].x), int(line[1].y), pr.WHITE)

    pr.end_drawing()
