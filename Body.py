from Transform import RigidBody
from Vector import vector

class MDynamics:
    def __init__(self):
        """ Initializes the physics engine"""

        self.rigidBodies = []

        self.drag = True
        self.dragv = 2

        self.gravity = True
        self.g = 9.81

        self.friction = True
        self.mu = 10

    def rec_rigidbody(self, x: int, y: int, width: int, height: int, mass: int):
        """ Creates a rectangle rigid body"""

        if mass < 0:
            Exception("mass should be at least 1")

        elif mass > 999999999999999999:
            Exception('mass should be smaller than 999999999999999999')
        
        else:
            rb = RigidBody(mass, width, height, vector(x, y))

            self.rigidBodies.append(rb)
            return rb

    def circle_rigidbody(self, x: int, y: int, radius: float, mass: int):
        """ Creates a circle rigid body"""


    def calculate_collisions(self):
        """Calculates Collision between bodies"""

        # TO DO
        # درست کردن این فوره (اشتباهه)

        for rb1 in self.rigidBodies:
            for rb2 in self.rigidBodies:
                if rb1 != rb2:
                    rb1.collision(rb2)

    def are_colliding(self, rb1, rb2):
        """Returns if 2 rigidbodies are colliding"""

        if rb1.position.x + rb1.width > rb2.position.x and rb1.position.x < rb2.position.x + rb2.width and rb1.position.y + rb1.height > rb2.position.y and rb1.position.y < rb2.position.y + rb2.height:
            return True

        else:
            return False

    def update_rigidbodies(self, dt: float):
        """Updates all rigid bodies position"""

        for rb in self.rigidBodies:
            if self.drag:
                rb.drag(self.dragv)

            if self.gravity:
                rb.applyForce(vector(0, 9.81 * rb.mass))

            if self.friction:
                rb.friction(self.mu)

            rb.update(dt)

    def update(rb):
        """Update this rigid body position"""

        if self.drag:
            rb.drag(self.dragv)

        if self.gravity:
            rb.applyForce(vector(0, 9.81 * rb.mass))

        if self.friction:
            rb.friction(self.mu)

        rb.update(dt)