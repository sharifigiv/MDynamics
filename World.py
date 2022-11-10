from Transform import *

import pyray as pr 
import time
from Vector import *
pr.init_window(1080, 720, "Physics")

Cube = RigidBody(0.001, 50, 50, [100, 60])
Cube2 = RigidBody(100, 50, 50, [100, 600])
# Cube3 = RigidBody(30, 50, 50, [200, 405])
RigidBodies = [Cube]

old_time = time.time()
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    new_time = time.time()
    dt = new_time - old_time
    old_time = new_time

    gravity = [0, 9.81]
    wind = 0

    if pr.is_mouse_button_down(0):
        wind = 10000

    if pr.is_mouse_button_down(1):
        wind = -10000

    Cube.applyForce(Vector(0, 9.81 * Cube.mass))
    Cube.applyForce(Vector(wind / Cube.mass, 0))
    Cube2.applyForce(Vector(0, 9.81 * Cube2.mass))
    Cube2.applyForce(Vector(wind / Cube2.mass, 0))
    # Cube3.applyForce([0,9.81*Cube3.mass])
    # Cube3.applyForce([(wind*Cube3.mass),0])
    Cube.collision(Cube2)
    Cube2.drag(0.2)
    # Cube.collision(Cube3)
    # Cube3.collision(Cube2)    
    Cube.update(dt)
    Cube2.update(dt)
    # Cube3.update(dt)

    Rec = pr.Rectangle(int(Cube.position[0]), int(Cube.position[1]), Cube.width, Cube.height)
    Rec2 = pr.Rectangle(int(Cube2.position[0]), int(Cube2.position[1]), Cube2.width, Cube2.height)
    # Rec3 = pr.Rectangle(int(Cube3.position[0]), int(Cube3.position[1]), Cube3.width, Cube3.height)
    
    pr.draw_rectangle_lines_ex(Rec, 5.0, pr.BLACK)
    pr.draw_rectangle_lines_ex(Rec2, 5.0, pr.RED)
    # pr.draw_rectangle_lines_ex(Rec3, 5.0, pr.BLACK)
    pr.draw_text(str(pr.get_fps()),20,20,22,pr.BLACK)
    pr.end_drawing()
