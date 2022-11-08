from Body import MDynamics
from Vector import vector

import pyray as pr
import time

Physics = MDynamics()
pr.init_window(1080, 720, "Physics")
Physics.friction = False

Cube = Physics.rec_rigidbody(100, 150, 50, 50, 3)
Cube2 = Physics.rec_rigidbody(100, 300, 55, 55, 4)

old_time = time.time()

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    new_time = time.time()
    dt = new_time - old_time
    old_time = new_time


    # Physics.calculate_collisions()
    Physics.update_rigidbodies(dt)

    Cube.collision(Cube2)

    Rec = pr.Rectangle(int(Cube.position.x), int(Cube.position.y), Cube.width, Cube.height)
    Rec2 = pr.Rectangle(int(Cube2.position.x), int(Cube2.position.y), Cube2.width, Cube2.height)
    
    pr.draw_rectangle_lines_ex(Rec, 5.0, pr.BLACK)
    pr.draw_rectangle_lines_ex(Rec2, 5.0, pr.RED)
    pr.draw_text(str(pr.get_fps()),20,20,22,pr.BLACK)
    pr.end_drawing()