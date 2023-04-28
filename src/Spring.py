from Vector import Vector
from Body import MDynamics
import pyray as pr
import math

SPRING_LENGTH = 300
SPRING_K = 50
SPRING_DAMPING = 0.2

class Spring:
    def __init__(self, node1, node2):
        self.particle1 = node1
        self.particle2 = node2
        self.length = SPRING_LENGTH
        self.k = SPRING_K
        self.damping = SPRING_DAMPING

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


pr.init_window(1080, 720, "Soft Body Boiii")
phy = MDynamics()

phy.circle_rigidbody('C1', 100, 300, 10, 1)
phy.circle_rigidbody('C2', 300, 100, 10, 1)
phy.circle_rigidbody('C3', 600, 100, 10, 1)
phy.circle_rigidbody('C4', 600, 400, 10, 1)

# C1 = Circle(10, 1, Vector(100, 100))
# C2 = Circle(10, 1, Vector(200, 100))
# C3 = Circle(10, 1, Vector(250, 200))
# C4 = Circle(10, 1, Vector(100, 200))

S1 = Spring(phy.rigidBodies['C1'], phy.rigidBodies['C2'])
S2 = Spring(phy.rigidBodies['C2'], phy.rigidBodies['C3'])
S3 = Spring(phy.rigidBodies['C3'], phy.rigidBodies['C4'])
S4 = Spring(phy.rigidBodies['C4'], phy.rigidBodies['C1'])
S5 = Spring(phy.rigidBodies['C1'], phy.rigidBodies['C3'])
S6 = Spring(phy.rigidBodies['C2'], phy.rigidBodies['C4'])

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    # C1.applyForce(Vector(0, 9.81))
    # C2.applyForce(Vector(0, 9.81))
    # C3.applyForce(Vector(0, 9.81))
    # C4.applyForce(Vector(0, 9.81))

    # C1.update(0.003)
    # C2.update(0.003)
    # C3.update(0.003)
    # C4.update(0.003)

    S1.update()
    S2.update()
    S3.update()
    S4.update()
    S5.update()
    S6.update()

    phy.calculate_collisions()
    phy.update_rigid_bodies(0.0004)

    pr.draw_circle(int(phy.rigidBodies['C1'].position.x), int(phy.rigidBodies['C1'].position.y), phy.rigidBodies['C1'].r, pr.WHITE)
    pr.draw_circle(int(phy.rigidBodies['C2'].position.x), int(phy.rigidBodies['C2'].position.y), phy.rigidBodies['C2'].r, pr.WHITE)
    pr.draw_circle(int(phy.rigidBodies['C3'].position.x), int(phy.rigidBodies['C3'].position.y), phy.rigidBodies['C3'].r, pr.WHITE)
    pr.draw_circle(int(phy.rigidBodies['C4'].position.x), int(phy.rigidBodies['C4'].position.y), phy.rigidBodies['C4'].r, pr.WHITE)

    pr.draw_line(int(S1.particle1.position.x), int(S1.particle1.position.y), int(
        S1.particle2.position.x), int(S1.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S2.particle1.position.x), int(S2.particle1.position.y), int(
        S2.particle2.position.x), int(S2.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S3.particle1.position.x), int(S3.particle1.position.y), int(
        S3.particle2.position.x), int(S3.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S4.particle1.position.x), int(S4.particle1.position.y), int(
        S4.particle2.position.x), int(S4.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S5.particle1.position.x), int(S5.particle1.position.y), int(
        S5.particle2.position.x), int(S5.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S6.particle1.position.x), int(S6.particle1.position.y), int(
        S6.particle2.position.x), int(S6.particle2.position.y), pr.WHITE)
        
    
    pr.end_drawing()
