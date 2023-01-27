from Vector import Vector
from Collision import *


class RigidBody:
    def __init__(self, mass, position):
        self.mass = mass

        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        self.mu = 0.8
        self.dt = 0

    def applyForce(self, force):
        # f = m * a
        # a = f / m

        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

    def drag(self, c):
        drag_direction = self.velocity
        drag_direction.multiply(-1)
        drag_direction = drag_direction.normalize()

        speed_sq = drag_direction.getMagnitude()
        drag_direction.setMagnitude(c * speed_sq * -1)

        self.applyForce(drag_direction)

    def friction(self, mu):
        friction = Vector(0, self.mass * 9.81)
        friction.multiplyBy(mu)
        friction.multiplyBy(-1)

        self.applyForce(friction)


class Poly(RigidBody):
    def __init__(self, sides, mass, position):
        self.sides = sides
        self.type = 'Poly'

        RigidBody.__init__(self, mass, position)

    def update(self, dt, edges=True):
        self.dt = dt
        if False:
            if self.position.y >= 720 - self.height:
                self.position.y = 720 - self.height
                self.friction(self.mu)
                self.velocity.y *= -1

            if self.position.x >= 1080 - self.width:
                self.position.x = 1080 - self.width
                self.friction(self.mu)
                self.velocity.x *= -1

            if self.position.x <= 0:
                self.position.x = 0
                self.friction(self.mu)
                self.velocity.x *= -1

            if self.position.y <= 0:
                self.position.y = 0
                self.friction(self.mu)
                self.velocity.y *= -1

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt


        new_p = self.velocity.x * dt
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt



        for side in self.sides:
            for line in side:
                line.x += new_p
                line.y += new_p

        self.acceleration = Vector(0, 0)

    def collision(self, R2):
        if R2.type == 'Circle':
            if poly_circle(self.sides, R2):
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1.add(mv2)

                deltav = self.velocity.subtract(R2.velocity)
                deltav.multiplyBy(R2.mass)
                deltamv = mv.subtract(deltav)

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                            deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                            self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

        elif R2.type == 'Poly':
            if poly_poly(R2.sides, self.sides):
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1.add(mv2)

                deltav = self.velocity.subtract(R2.velocity)
                deltav.multiplyBy(R2.mass)
                deltamv = mv.subtract(deltav)

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                            deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                            self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

class Circle(RigidBody):
    def __init__(self,r, mass, position):
        self.r = r
        self.type = 'Circle'
        RigidBody.__init__(self, mass, position)

    def collision(self,R2):
        if R2.type == 'Circle':
            p1 = self.position
            p2 = R2.position

            dx = p1.x - p2.x
            dy = p1.y - p2.y
            dist = (dx**2 + dy**2)**0.5

            if dist <= self.r + R2.r:
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1.add(mv2)

                deltav = self.velocity.subtract(R2.velocity)
                deltav.multiplyBy(R2.mass)
                deltamv = mv.subtract(deltav)

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                            deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                            self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

        elif R2.type == 'Poly':
            if poly_circle(R2.sides, self):
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1.add(mv2)

                deltav = self.velocity.subtract(R2.velocity)
                deltav.multiplyBy(R2.mass)
                deltamv = mv.subtract(deltav)

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                            deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                            self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

    
    def update(self, dt, edges=True):
        self.dt = dt
        if edges:
            if self.position.y >= 720 - self.r:
                self.position.y = 720 - self.r
                self.friction(self.mu)
                self.velocity.y *= -1

            if self.position.x >= 1080 - self.r:
                self.position.x = 1080 - self.r
                self.friction(self.mu)
                self.velocity.x *= -1

            if self.position.x <= 0:
                self.position.x = 0
                self.friction(self.mu)
                self.velocity.x *= -1

            if self.position.y <= 0:
                self.position.y = 0
                self.friction(self.mu)
                self.velocity.y *= -1

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        self.acceleration = Vector(0, 0)