import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as v
import src.Spring as Spring
import src.SoftBody as sf
import src.Body as MDynamics
import src.Collision as collision
import pyray as pr 

pr.init_window(1080, 920, "Spring Lab")
phy = MDynamics.MDynamics()

m = 50
m1 = 100
m2 = 500

c1 = phy.circle_rigidbody("C1", 1080 // 2, 0, 1, 10000000)
c2 = phy.circle_rigidbody("C2", 1080 // 2, 0, 1, 10000000)
c3 = phy.circle_rigidbody("C3", 1080 // 2, 0, 1, 10000000)

r1 = phy.poly_rigidBody("R1", 1080 // 2, 300, m, [[v.Vector(1080 // 2 - 50, 300), v.Vector(1080 // 2 + 100 - 50, 300)], [v.Vector(1080 // 2 + 100 - 50, 300), v.Vector(1080 // 2 + 100 - 50, 300 + 100)], [v.Vector(1080 // 2 + 100 - 50, 300 + 100), v.Vector(1080 // 2 - 50, 300 + 100)], [v.Vector(1080 // 2 - 50, 300 + 100), v.Vector(1080 // 2 - 50, 300)]])
r2 = phy.poly_rigidBody("R2", 1080 // 2, 300, m1, [[v.Vector(1080 // 2 - 50, 300), v.Vector(1080 // 2 + 100 - 50, 300)], [v.Vector(1080 // 2 + 100 - 50, 300), v.Vector(1080 // 2 + 100 - 50, 300 + 100)], [v.Vector(1080 // 2 + 100 - 50, 300 + 100), v.Vector(1080 // 2 - 50, 300 + 100)], [v.Vector(1080 // 2 - 50, 300 + 100), v.Vector(1080 // 2 - 50, 300)]])
r3 = phy.poly_rigidBody("R3", 1080 // 2, 300, m2, [[v.Vector(1080 // 2 - 50, 300), v.Vector(1080 // 2 + 100 - 50, 300)], [v.Vector(1080 // 2 + 100 - 50, 300), v.Vector(1080 // 2 + 100 - 50, 300 + 100)], [v.Vector(1080 // 2 + 100 - 50, 300 + 100), v.Vector(1080 // 2 - 50, 300 + 100)], [v.Vector(1080 // 2 - 50, 300 + 100), v.Vector(1080 // 2 - 50, 300)]])

s = Spring.Spring(c1, r1, 300, 100, 4)
s1 = Spring.Spring(c2, r2, 300, 100, 6)
s2 = Spring.Spring(c3, r3, 300, 100, 50)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    s.update()
    s1.update()
    s2.update()

    phy.update_rigid_bodies(0.003)

    c1.velocity = v.Vector(0, 0)
    c2.velocity = v.Vector(0, 0)
    c3.velocity = v.Vector(0, 0)

    for l in r1.sides:
        pr.draw_line(int(l[0].x) - 125, int(l[0].y), int(l[1].x) - 125 , int(l[1].y), pr.BLACK)

    for l in r2.sides:
        pr.draw_line(int(l[0].x) - 125 + 75 + 100, int(l[0].y), int(l[1].x) - 125 + 75 + 100, int(l[1].y), pr.BLACK)

    for l in r3.sides:
        pr.draw_line(int(l[0].x) - 125 + 75 + 100 + 75 + 100, int(l[0].y), int(l[1].x) - 125 + 75 + 100 + 75 + 100, int(l[1].y), pr.BLACK)

    pr.draw_line(int(c1.position.x) - 125, int(c1.position.y) - 100, int(r1.position.x) - 125, int(r1.position.y), pr.BLACK)
    pr.draw_line(int(c2.position.x) - 125 + 75 + 100, int(c2.position.y) - 100, int(r2.position.x) - 125 + 100 + 75, int(r2.position.y), pr.BLACK)
    pr.draw_line(int(c3.position.x) - 125 + 75 + 100 + 75 + 100, int(c3.position.y) - 100, int(r3.position.x) - 125 + 100 + 75 + 75 + 100, int(r3.position.y), pr.BLACK)

    pr.end_drawing()
