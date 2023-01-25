from Transform import *
from Vector import Vector

# ما عبدل را راضی کردیم

class MDynamics:
    def __init__(self):
        """ Initializes the physics engine"""

        self.rigidBodies = {}

        self.drag = True
        self.dragv = 6

        self.gravity = True
        self.g = 98.1

        self.friction = True
        self.mu = -1

    def poly_rigidBody(self, name:str, x: int, y: int, mass: int, sides: list):
        """ Creates a rectangle rigid body"""

        if mass < 0:
            Exception("mass should be at least 1")

        elif mass > 999999999999999999:
            Exception('mass should be smaller than 999999999999999999')
        
        else:
            self.rigidBodies[name] = Poly(sides, mass, Vector(x, y))

    def circle_rigidbody(self, name: str, x: int, y: int, radius: float, mass: int):
        """ Creates a circle rigid body"""

        if mass < 0:
            Exception("mass should be at least 1")

        elif mass > 999999999999999999:
            Exception('mass should be smaller than 999999999999999999')
        
        else:
            self.rigidBodies[name] = Circle(radius, mass, Vector(x, y))

    def calculate_collisions(self):
        """Calculates Collision between bodies"""
        keys = list(self.rigidBodies.keys())
        for rb1_name in keys:
            for rb2_name in keys[keys.index(rb1_name):]:
                    self.rigidBodies[rb1_name].collision(self.rigidBodies[rb2_name])


    def are_colliding(self, rb1, rb2):
        """Returns if 2 rigidbodies are colliding"""

        if rb1.position.x + rb1.width > rb2.position.x and rb1.position.x < rb2.position.x + rb2.width and rb1.position.y + rb1.height > rb2.position.y and rb1.position.y < rb2.position.y + rb2.height:
            return True

        else:
            return False

    def update_rigid_bodies(self, dt: float):
        """Updates all rigid bodies position"""

        for rb in list(self.rigidBodies.keys()):
            RigidBody_object = self.rigidBodies[rb]
            if self.drag:
                RigidBody_object.drag(self.dragv)

            if self.gravity:
                RigidBody_object.applyForce(Vector(0, 98.1 * RigidBody_object.mass))

            RigidBody_object.update(dt)

    def update(self, rb, dt):
        """Update this rigid body position"""

        if self.drag:
            rb.drag(self.dragv)

        if self.gravity:
            rb.applyForce(Vector(0, 9.81 * rb.mass))

        rb.update(dt)
