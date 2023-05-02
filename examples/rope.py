import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as vec
import src.Spring as Spring
import src.Body as MDynamics
import src.Collision as collision
import pyray as pr 

pr.init_window(1080, 720, "Rope 2D")
phy = MDynamics.MDynamics(1080, 720)

phy.gravity = False

C1 = phy.circle_rigidbody("C1", 1080 // 2, 720 // 2 - 200, 15, 1)
C2 = phy.circle_rigidbody("C2", 1080 // 2, 720 // 2 + 150 - 200, 15, 1)
C3 = phy.circle_rigidbody("C3", 1080 // 2, 720 // 2 + 250 - 200 , 15, 1)

S1 = Spring.Spring(C1, C2, 150, 60, 0.4)
S2 = Spring.Spring(C2, C3, 150, 60, 0.4)

pause = False

while not pr.window_should_close():   
    if pr.is_key_pressed(32):
        if pause:
            pause = False

        else:
            pause = True

    if pr.is_mouse_button_down(0):
        pause = True
        if collision.circle_point(vec.Vector(pr.get_mouse_x(), pr.get_mouse_y()), C2):
            C2.position.x = pr.get_mouse_x()
            C2.position.y = pr.get_mouse_y()

        elif collision.circle_point(vec.Vector(pr.get_mouse_x(), pr.get_mouse_y()), C3):
            C3.position.x = pr.get_mouse_x()
            C3.position.y = pr.get_mouse_y()            

    pr.begin_drawing()
    pr.clear_background(pr.Color(236, 240, 241, 255))

    if not pause:
        C2.applyForce(vec.Vector(0, 98.1))
        C3.applyForce(vec.Vector(0, 98.1))

        phy.update_rigid_bodies(0.002)

        C1.velocity = vec.Vector(0, 0)
        C1.acceleration = vec.Vector(0, 0)

        S1.update()
        S2.update()

    pr.draw_line_ex(pr.Vector2(int(S1.particle1.position.x), int(S1.particle1.position.y)), pr.Vector2(int(S1.particle2.position.x), int(S1.particle2.position.y)), 3, pr.Color(142, 68, 173, 255))
    pr.draw_line_ex(pr.Vector2(int(S2.particle1.position.x), int(S2.particle1.position.y)), pr.Vector2(int(S2.particle2.position.x), int(S2.particle2.position.y)), 3, pr.Color(142, 68, 173, 255))

    pr.draw_circle(int(C1.position.x), int(C1.position.y), 15, pr.Color(241, 196, 15, 255))
    pr.draw_circle(int(C2.position.x), int(C2.position.y), 15, pr.Color(241, 196, 15, 255))
    pr.draw_circle(int(C3.position.x), int(C3.position.y), 15, pr.Color(241, 196, 15, 255))

    pr.draw_text(str("Paused: ") + str(pause), 25, 30, 24, pr.Color(44, 62, 80, 255))

    pr.end_drawing()
