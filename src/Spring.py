from Vector import Vector
import math

SPRING_LENGTH = 50
SPRING_K = 300
SPRING_DAMPING = 0.4

class Spring:
    def __init__(self, node1, node2, spring_length, spring_k, spring_damping):
        self.particle1 = node1
        self.particle2 = node2
        self.length = spring_length
        self.k = spring_k
        self.damping = spring_damping

    def update(self):
        dx = self.particle2.position.x - self.particle1.position.x
        dy = self.particle2.position.y - self.particle1.position.y
        distance = math.sqrt(dx*dx + dy*dy)
        force = self.k * (distance - self.length)

        relativeVelocityX = self.particle2.velocity.x - self.particle1.velocity.x
        relativeVelocityY = self.particle2.velocity.y - self.particle1.velocity.y
        dampingForceX = self.damping * relativeVelocityX
        dampingForceY = self.damping * relativeVelocityY

        fx = force * dx / distance
        fy = force * dy / distance

        self.particle1.applyForce(Vector(fx, fy))
        self.particle1.applyForce(Vector(dampingForceX, dampingForceY))
        self.particle2.applyForce(Vector(-dampingForceX, -dampingForceY))

        self.particle2.applyForce(Vector(-fx, -fy))
