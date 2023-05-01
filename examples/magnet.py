import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as vec
import src.Spring as Spring
import src.Body as MDynamics
import src.Collision as collision
import pyray as pr
import random
import math

WIDTH = 1080
HEIGHT = 720

physics = MDynamics.MDynamics()
physics.gravity = False


for i in range(75):
    physics.circle_rigidbody(str(i), random.randint(0, WIDTH), random.randint(0, HEIGHT), 5, 1)

pr.init_window(WIDTH, HEIGHT, "Magnet 2D")

magnet = physics.poly_rigidBody("magnet", WIDTH, HEIGHT//2, 5, [[vec.Vector(WIDTH, HEIGHT//2 - 100), vec.Vector(WIDTH, HEIGHT//2)], [vec.Vector(WIDTH, HEIGHT//2), vec.Vector(800, HEIGHT//2)], [vec.Vector(800, HEIGHT//2), vec.Vector(800, HEIGHT//2 - 100)], [vec.Vector(800, HEIGHT//2 - 100), vec.Vector(WIDTH, HEIGHT//2 - 100)]])

while not pr.window_should_close():
    key = pr.get_key_pressed()

    physics.rigidBodies["magnet"].acceleration = vec.Vector(0,0)
    physics.rigidBodies["magnet"].velocity = vec.Vector(0,0)

    physics.update_rigid_bodies(0.003)

    pr.begin_drawing()
    pr.clear_background((255, 255, 255))

    for rb in list(physics.rigidBodies.values()):
        if rb.type == 'Circle':
            line = [physics.rigidBodies["magnet"].center, rb.position]
            dx = (physics.rigidBodies["magnet"].center.x - rb.position.x) ** 2
            dy = (physics.rigidBodies["magnet"].center.y - rb.position.y) ** 2
            dist = math.sqrt(dx + dy)
            kool, point, final1, final2 = collision.poly_line(physics.rigidBodies["magnet"].sides, physics.rigidBodies["magnet"].center, rb.position)
            if collision.circle_point(point, rb):
                rb.acceleration = vec.Vector(0,0)
                rb.velocity = vec.Vector(0,0)
            else:
                f = vec.Vector(point.x - rb.position.x, point.y - rb.position.y)
                f.x *= 1 / (dist / 1000)
                f.y *= 1 / (dist / 1000)
                rb.applyForce(f)

    for rb in list(physics.rigidBodies.values()):
        if rb.type == "Circle":
            pr.draw_circle(int(rb.position.x), int(rb.position.y), rb.r, (255, 90, 25))
        if (rb.type == 'Poly'):
            for line in rb.sides:
                # pr.draw_line(int(line[0].x), int(line[0].y), int(
                #     line[1].x), int(line[1].y), (1, 46, 101))
                pr.draw_line_ex(pr.Vector2(line[0].x, line[0].y), pr.Vector2(line[1].x, line[1].y), 5, (1, 46, 101))
    pr.end_drawing()