import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as vec
import src.Spring as Spring
import src.Body as MDynamics
import src.Collision as collision
import pyray as pr
import random

WIDTH = 800
HEIGHT = 600

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
temperature = 100
physics = MDynamics.MDynamics()
physics.gravity = False

for i in range(50):
    physics.circle_rigidbody(str(i), random.randint(0, WIDTH), random.randint(0, HEIGHT), 5, 1)

pr.init_window(WIDTH, HEIGHT, "Temperature 2D")

while not pr.window_should_close():
    key = pr.get_key_pressed()
    if key == 265:
        temperature += 10
    elif key == 264:
        if temperature < 10:
            temperature = 0
        else:
            temperature -= 10

    for rb in list(physics.rigidBodies.values()):
        rb.velocity.x = random.randint(-temperature, temperature)
        rb.velocity.y = random.randint(-temperature, temperature)
    
    physics.update_rigid_bodies(0.005)

    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    for rb in list(physics.rigidBodies.values()):
        pr.draw_circle(int(rb.position.x), int(rb.position.y), rb.r, pr.Color(39, 174, 96,255))
    
    pr.draw_text("Temperature: "+str(temperature/10), 25, 30, 24, pr.WHITE)
    
    pr.end_drawing()