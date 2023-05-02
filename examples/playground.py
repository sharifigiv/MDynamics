import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

from src.Vector import Vector, rotate
from src.Transform import RigidBody, Poly, Circle
from src.Collision import * 
from src.Body import MDynamics
from ui import Button

import pyray as pr
import time

Phy = MDynamics(1280, 720)
pr.init_window(1280, 720, "Playground")

Phy.drag = True; Phy.friction = True

old_time = time.time()
paused = False

Object_num = 0
Object_Choosen = ''

Object_power = None 
power = []
powering = False

mouse_pos = [0, 0]
mouse_clicked = False

drawing_point = [1280//2, 720 //2]

def draw_poly(n, point1x, point1y):
    global Object_num

    Object_num += 1 
    sides = []
    new_line = [Vector(point1x, point1y), Vector(point1x + 40, point1y)]

    angle = -1 * (180 - (((n - 2) * 180)//n))

    sides.append(new_line)
    for side in range(5):
        last_point_2 = sides[len(sides) - 1][1]
        last_point_1 = sides[len(sides) - 1][0]

        line_last = last_point_2.subtract(last_point_1)
        final_point = line_last.add(last_point_2)

        final_line = rotate(last_point_2, final_point, angle)
        sides.append([last_point_2, final_line])

    return sides

# ui
circle_btn = Button(750, 50, 75, 75, 'Circle')
poly_btn3 = Button(850, 50, 75, 75, 'Poly 3')
poly_btn4 = Button(950, 50, 75, 75, 'Poly 4')
poly_btn5 = Button(1050, 50, 75, 75, 'Poly 5')
poly_btn6 = Button(1150, 50, 75, 75, 'Poly 6')

clear_btn = Button(100, 50, 100, 75, 'Clear All')

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    new_time = time.time()
    dt = new_time - old_time
    old_time = new_time

    mouse_pos = [pr.get_mouse_x(), pr.get_mouse_y()]
    mouse_clicked = pr.is_mouse_button_pressed(0)
    mouse_down = pr.is_mouse_button_down(0)

    key = pr.get_key_pressed()

    if key == 32:
        if paused:
            paused = False

        else:
            paused = True

    if pr.is_mouse_button_pressed(1):
        for rb in list(Phy.rigidBodies.keys()):
            if(Phy.rigidBodies[rb].type == 'Poly'):
                if poly_point(Phy.rigidBodies[rb].sides, Vector(mouse_pos[0], mouse_pos[1])):
                    del Phy.rigidBodies[rb]
                    break

    if pr.is_mouse_button_down(0) and mouse_pos[1] > 110:
        powering = True 
        power.append(mouse_pos)

    else:
        if powering:
            powering = False
            power_vec = Vector(-(mouse_pos[0] - power[0][0]), -(mouse_pos[1] - power[0][1]))

            if poly_btn6.clicked:
                Object_num += 1
                ss = draw_poly(6, mouse_pos[0], mouse_pos[1])

                Phy.poly_rigidBody('poly' + str(Object_num), mouse_pos[0], mouse_pos[1], 40, ss) 
                Phy.rigidBodies['poly' + str(Object_num)].velocity.x = power_vec.x
                Phy.rigidBodies['poly' + str(Object_num)].velocity.y = power_vec.y

            power = []

            if poly_btn5.clicked:
                Object_num += 1
                ss = draw_poly(5, mouse_pos[0], mouse_pos[1])

                Phy.poly_rigidBody('poly' + str(Object_num), mouse_pos[0], mouse_pos[1], 40, ss) 
                Phy.rigidBodies['poly' + str(Object_num)].velocity.x = power_vec.x
                Phy.rigidBodies['poly' + str(Object_num)].velocity.y = power_vec.y

            power = []

            if poly_btn3.clicked:
                Object_num += 1
                ss = draw_poly(3, mouse_pos[0], mouse_pos[1])

                Phy.poly_rigidBody('poly' + str(Object_num), mouse_pos[0], mouse_pos[1], 40, ss) 
                Phy.rigidBodies['poly' + str(Object_num)].velocity.x = power_vec.x
                Phy.rigidBodies['poly' + str(Object_num)].velocity.y = power_vec.y

            power = []

            if poly_btn4.clicked:
                Object_num += 1
                ss = draw_poly(4, mouse_pos[0], mouse_pos[1])

                Phy.poly_rigidBody('poly' + str(Object_num), mouse_pos[0], mouse_pos[1], 40, ss) 
                Phy.rigidBodies['poly' + str(Object_num)].velocity.x = power_vec.x
                Phy.rigidBodies['poly' + str(Object_num)].velocity.y = power_vec.y

            if circle_btn.clicked:
                Object_num += 1
                Phy.circle_rigidbody('circle' + str(Object_num), mouse_pos[0], mouse_pos[1], 30,100)
                Phy.rigidBodies['circle' + str(Object_num)].velocity.x = power_vec.x
                Phy.rigidBodies['circle' + str(Object_num)].velocity.y = power_vec.y

            power = []

    poly_btn6.update(mouse_pos, mouse_clicked)
    poly_btn5.update(mouse_pos, mouse_clicked)
    poly_btn4.update(mouse_pos, mouse_clicked)
    poly_btn3.update(mouse_pos, mouse_clicked)
    clear_btn.update(mouse_pos, mouse_clicked)
    circle_btn.update(mouse_pos, mouse_clicked)

    if clear_btn.clicked:
        Phy.rigidBodies.clear()

    poly_btn6.show()
    poly_btn5.show()
    poly_btn4.show()
    poly_btn3.show()
    clear_btn.show()
    circle_btn.show()

    if powering:
        pr.draw_line(power[0][0], power[0][1], mouse_pos[0], mouse_pos[1], pr.Color(0, 0, 0, 50))

    if not paused:
        Phy.calculate_collisions()
        Phy.update_rigid_bodies(dt)
        
    for rb in list(Phy.rigidBodies.keys()):
        if(Phy.rigidBodies[rb].type == 'Poly'):
            for line in Phy.rigidBodies[rb].sides:
                pr.draw_line(int(line[0].x), int(line[0].y), int(line[1].x), int(line[1].y), pr.BLACK)

        elif(Phy.rigidBodies[rb].type == 'Circle'):
            m = Phy.rigidBodies

            pr.draw_circle_lines(int(m[rb].position.x), int(m[rb].position.y), m[rb].r, pr.BLACK)
    
    pr.draw_text(str(pr.get_fps()),10,10,22,pr.BLACK)
    pr.draw_circle(drawing_point[0], drawing_point[1], 2.0, pr.RED)
    pr.end_drawing()
