from Body import MDynamics
import pyray as pr
import time
from Vector import Vector
Physics = MDynamics()
pr.init_window(1080, 720, "Physics")

Physics.make_rec_rigidBody("Cube", 0, 500, 50, 50, 30)
Physics.make_rec_rigidBody("Cube2", 0, 300, 55, 55, 40)
old_time = time.time()

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    new_time = time.time()
    dt = new_time - old_time
    old_time = new_time

    if(pr.is_mouse_button_down(1)):
        Physics.rigidBodies["Cube"].applyForce(Vector(20,0))
    Physics.calculate_collisions()
    Physics.update_rigidbodies(dt)

    Rec = pr.Rectangle(int(Physics.rigidBodies["Cube"].position.x), int(
        Physics.rigidBodies["Cube"].position.y), Physics.rigidBodies["Cube"].width, Physics.rigidBodies["Cube"].height)
    Rec2 = pr.Rectangle(int(Physics.rigidBodies["Cube2"].position.x), int(
        Physics.rigidBodies["Cube2"].position.y), Physics.rigidBodies["Cube2"].width, Physics.rigidBodies["Cube2"].height)

    pr.draw_rectangle_lines_ex(Rec, 5.0, pr.BLACK)
    pr.draw_rectangle_lines_ex(Rec2, 5.0, pr.RED)
    pr.draw_text(str(pr.get_fps()), 20, 20, 22, pr.BLACK)
    pr.end_drawing()
