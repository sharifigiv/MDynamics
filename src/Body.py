from Transform import *
from Vector import Vector

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

    def update_rigid_bodies(self, dt: float):
        """Updates all rigid bodies position"""

        for rb in list(self.rigidBodies.keys()):
            RigidBody_object = self.rigidBodies[rb]
            if self.drag:
                RigidBody_object.drag(self.dragv)

            if self.gravity:
                RigidBody_object.applyForce(Vector(0, 98.1 * RigidBody_object.mass))
            RigidBody_object.update(dt)
