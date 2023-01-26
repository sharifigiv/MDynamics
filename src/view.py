from Body import MDynamics
import pyray as pr
import time
from Vector import Vector, rotate

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
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0] + 20, mouse_pos[1])]
        sides.append(new_line)
        for i in range(5):
            last_point = sides[len(sides) - 1][1]

            last_line_vector = sides[len(sides) - 1][1].subtract(sides[len(sides) - 1][0])
            point2 = last_line_vector.add(last_point)

            final_line = rotate(last_point, point2, 108)
            sides.append(final_line)

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)
    if key == 67:
        i += 1
        Physics.circle_rigidbody('circle' + str(i), mouse_pos[0], mouse_pos[1], 30,100)
        
    if key == 32:
        if paused:
            paused = False
        else:
            paused = True  

    if not paused:
        
        Physics.calculate_collisions()
        Physics.update_rigid_bodies(dt)
        
    for rb in list(Physics.rigidBodies.keys()):
        if(Physics.rigidBodies[rb].type == 'Poly'):
            for line in Physics.rigidBodies[rb].sides:
                pr.draw_line(int(line[0].x), int(line[0].y), int(line[1].x), int(line[1].y), pr.BLACK)
        elif(Physics.rigidBodies[rb].type == 'Circle'):
            m = Physics.rigidBodies

            pr.draw_circle_lines(int(m[rb].position.x), int(m[rb].position.y), m[rb].r, pr.BLACK)
            pr.draw_text(str(pr.get_fps()),10,10,22,pr.BLACK)

    pr.end_drawing()