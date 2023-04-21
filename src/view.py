from Body import MDynamics
import pyray as pr
import time
from Vector import Vector, rotate

pr.init_window(1280, 720, "MDynamics")
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
        
    if key == 51:  
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]
        
        sides.append(new_line)
        for side in range(2):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -120)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)
    
    if key == 52:
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]

        sides.append(new_line)
        for side in range(3):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -90)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)
    
    if key == 53:     
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]

        
        sides.append(new_line)
        for side in range(4):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -72)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)

    if key == 54:
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]
        
        sides.append(new_line)
        for side in range(5):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -60)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)
    
    if key == 55:
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]
        
        sides.append(new_line)
        for side in range(6):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -52)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)
    
    if key == 56:
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]
        
        sides.append(new_line)
        for side in range(7):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -45)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)
    
    if key == 57:
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]
        
        sides.append(new_line)
        for side in range(8):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, -40)
            sides.append([last_point_2, final_line])

        Physics.poly_rigidBody('poly' + str(i), mouse_pos[0], mouse_pos[1], 30,sides)

    if key == 82:
        i += 1
        sides = []
        new_line = [Vector(mouse_pos[0], mouse_pos[1]), Vector(mouse_pos[0]+40, mouse_pos[1]+0)]
        
        sides.append(new_line)
        for side in range(5):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2
                    
            final_line = rotate(last_point_2, final_point, -60)
            sides.append([last_point_2, final_line])

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
