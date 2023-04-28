import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as vec
import src.Spring as Spring
import src.SoftBody as sf
import src.Body as MDynamics
import src.Collision as collision
import pyray as pr 

pr.init_window(1080, 720, "Cloth 2D")
phy = MDynamics.MDynamics()

s = sf.SoftBody(100, 5, 5, vec.Vector(400, 100), phy)
s.create_particles()
s.create_springs()

pause = False

pinned = ["C1", "C6", "C11", "C21", "C16"]

while not pr.window_should_close():
    if pr.is_key_pressed(32):
        if pause:
            pause = False

        else:
            pause = True

    if pr.is_mouse_button_pressed(0):
        pos = [pr.get_mouse_x(), pr.get_mouse_y()]

        for rb in list(phy.rigidBodies.keys()):
            if pr.check_collision_point_circle(pr.Vector2(pos[0], pos[1]), pr.Vector2(phy.rigidBodies[rb].position.x, phy.rigidBodies[rb].position.y), 5):
                if rb not in pinned:
                    pinned.append(rb)
                break

    if pr.is_mouse_button_pressed(1):
        pos = [pr.get_mouse_x(), pr.get_mouse_y()]

        for rb in list(phy.rigidBodies.keys()):
            if pr.check_collision_point_circle(pr.Vector2(pos[0], pos[1]), pr.Vector2(phy.rigidBodies[rb].position.x, phy.rigidBodies[rb].position.y), 5):
                if rb in pinned:
                    pinned.remove(rb)
                break

    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    s.draw_particles()
    s.draw_springs()

    if not pause:
        s.update_springs()

        for rb in list(phy.rigidBodies.keys()):
            if rb in pinned:
                pass
            else:
                phy.rigidBodies[rb].applyForce(vec.Vector(0, 998.1))
                phy.rigidBodies[rb].update(0.003)

    pr.end_drawing()
