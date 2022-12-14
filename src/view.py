from Body import MDynamics
import pyray as pr
import time
import Vector

pr.init_window(1280, 720, "View")
Physics = MDynamics()

old_time = time.time()

paused = True

i = 0
mouse_pos = [0, 0]
Physics.drag = True
Physics.friction = False

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    new_time = time.time()
    dt = new_time - old_time
    old_time = new_time

    key = pr.get_key_pressed()


    if pr.is_mouse_button_down(0):
        mouse_pos[0] = pr.get_mouse_x()
        mouse_pos[1] = pr.get_mouse_y()

    if key == 82:
        i += 1
        Physics.make_pol_rigidBody('Cube' + str(i), mouse_pos[0], mouse_pos[1], 1000, "polygon",[100])
    if key == 32:
        if paused:
            paused = False
        else:
            paused = True

    if not paused:
        
        Physics.calculate_collisions()
        Physics.update_rigid_bodies(dt)
        
        # Physics.calculate_collisions()
        # Physics.update_rigid_bodies(dt)
        # Physics.calculate_collisions()
    for rb in list(Physics.rigidBodies.keys()):
        m = Physics.rigidBodies

        rec = pr.Rectangle(m[rb].position.x, m[rb].position.y, 1 * 100, 1 * 100 )
        pr.draw_rectangle_lines_ex(rec, 1.0, pr.BLACK)
        pr.draw_text(str(pr.get_fps()),10,10,22,pr.BLACK)

    pr.end_drawing()    