import os; import sys; sys.path.insert(1, os.path.join(sys.path[0], '..'))
sys.path.append('./src/')

import src.Vector as vec
import src.Spring as Spring
import src.Body as MDynamics
import src.Collision as collision
import src.Transform as transform
import pyray as pr
from random import randrange, uniform
from math import sin, cos, pi, radians

physics = MDynamics.MDynamics()
pr.init_window(1600, 900, "Planets 2D")

class star(transform.RigidBody):
    instances = []
    def __init__(self, size, x, y, colour):
        self.__class__.instances.append(self)
        self.size = size
        self.x = x
        self.y = y
        self.colour = colour

    def generate(self):
        pr.draw_circle(int(self.x), int(self.y), self.size*10, self.colour)

class satellite(transform.RigidBody):
    instances = []
    def __init__(self, parent, size, distance, velocity, colour):
        self.__class__.instances.append(self)
        self.size = size/3
        self.radius = distance*70
        self.velocity = velocity/10000
        self.colour = colour
        self.parent = parent
        self.center_of_rotation_x = parent.x
        self.center_of_rotation_y = parent.y
        self.angle = radians(randrange(0,360))
        self.x = self.center_of_rotation_x + self.radius * cos(self.angle)
        self.y = self.center_of_rotation_y - self.radius * sin(self.angle)
    
    
    def calculateMovement(self):
        self.center_of_rotation_x = self.parent.x #updates position of the body it's circling
        self.center_of_rotation_y = self.parent.y
        self.x = self.center_of_rotation_x + self.radius * cos(self.angle) # generate position based on what we're orbiting + our angle
        self.y = self.center_of_rotation_y - self.radius * sin(self.angle)
        pr.draw_circle(int(self.x), int(self.y), self.radius/25, self.colour) # draw to the screen
        self.angle = self.angle + self.velocity # New angle, we add angular velocity
        self.x = self.x + self.radius * self.velocity * cos(self.angle + pi / 2) # New x
        self.y = self.y - self.radius * self.velocity * sin(self.angle + pi / 2) # New y


sun = star(5, 1600/2, 900/2, (255,255,0))

#Planets
mercury = satellite(sun, 1, 1, -48, (219,206,202))
venus = satellite(sun, 3, 2, 35, (150,131,150))
earth = satellite(sun, 4, 3, 30, (0,0,205))
mars = satellite(sun, 2, 4, -24, (193,68,14))
jupiter = satellite(sun, 8, 6, 13, (227,110,75))
saturn = satellite(sun, 7, 7, -10, (206,184,184))
uranus = satellite(sun, 6, 8, -7, (213,251,252))
neptune = satellite(sun, 5, 9, 5, (91,93,223))
#Moons
mercury_moon = satellite(mercury, 0.6, 0.1, 200, (150,131,150))
venus_moon = satellite(venus, 0.8, 0.3, -180, (150,131,150))
venus_moon = satellite(venus, 1, 0.4, 200, (150,131,150))
earth_moon = satellite(earth, 0, 0.2, -300, (0,0,0))
mars_moon = satellite(mars, 0.4, 0.25, -380, (150,131,150))
mars_moon = satellite(mars, 0.7, 0.4, 240, (150,131,150))
jupiter_moon = satellite(jupiter, 2, 0.6, 200, (150,131,150))
jupiter_moon = satellite(jupiter, 1.4, 0.45, -380, (150,131,150))
jupiter_moon = satellite(jupiter, 0.7, 0.6, 240, (150,131,150))
saturn_moon = satellite(saturn, 2, 0.6, 200, (150,131,150))
saturn_moon = satellite(saturn, 1.4, 0.45, -380, (150,131,150))
uranus_moon = satellite(uranus, 2, 0.6, 200, (150,131,150))
uranus_moon = satellite(uranus, 1.4, 0.45, -380, (150,131,150))
uranus_moon = satellite(uranus, 0.7, 0.6, 240, (150,131,150))
neptune_moon = satellite(neptune, 1.4, 0.45, -380, (150,131,150))
neptune_moon = satellite(neptune, 0.7, 0.6, 240, (150,131,150))
for i in range(0,200):
    bg_stars = star(uniform(1.0,2.0)/25, randrange(0,1600), randrange(0,900), (randrange(220,255),randrange(220,255),randrange(220,255)))

for i in range(0,300):
    asteroid = satellite(sun, uniform(0.1,1.0)/10, uniform(4.5, 5.2)/1.0099, randrange(20,22), (219,206,202))

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    [star.generate() for star in star.instances] #Draw stars
    [satellite.calculateMovement() for satellite in satellite.instances] #Draw satellites



    
    pr.end_drawing()