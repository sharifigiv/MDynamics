from Vector import Vector
from Transform import Circle
import pyray as pr
import math

SPRING_LENGTH = 100
SPRING_K = 0.1
SPRING_DAMPING = 0.07

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

C1 = Circle(10, 1, Vector(100, 100))
C2 = Circle(10, 1, Vector(200, 100))
C3 = Circle(10, 1, Vector(250, 250))
C4 = Circle(10, 1, Vector(100, 200))

S1 = Spring(C1, C2)
S2 = Spring(C2, C3)
S3 = Spring(C3, C4)
S4 = Spring(C4, C1)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)

    # C1.applyForce(Vector(0, 9.81))
    # C2.applyForce(Vector(0, 9.81))
    # C3.applyForce(Vector(0, 9.81))
    # C4.applyForce(Vector(0, 9.81))

    C1.update(0.003)
    C2.update(0.003)
    C3.update(0.003)
    C4.update(0.003)

    S1.update()
    S2.update()
    S3.update()
    S4.update()

    pr.draw_circle(int(C1.position.x), int(C1.position.y), C1.r, pr.WHITE)
    pr.draw_circle(int(C2.position.x), int(C2.position.y), C2.r, pr.WHITE)
    pr.draw_circle(int(C3.position.x), int(C3.position.y), C3.r, pr.WHITE)
    pr.draw_circle(int(C4.position.x), int(C4.position.y), C4.r, pr.WHITE)

    pr.draw_line(int(S1.particle1.position.x), int(S1.particle1.position.y), int(S1.particle2.position.x), int(S1.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S2.particle1.position.x), int(S2.particle1.position.y), int(S2.particle2.position.x), int(S2.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S3.particle1.position.x), int(S3.particle1.position.y), int(S3.particle2.position.x), int(S3.particle2.position.y), pr.WHITE)
    pr.draw_line(int(S4.particle1.position.x), int(S4.particle1.position.y), int(S4.particle2.position.x), int(S4.particle2.position.y), pr.WHITE)

    pr.end_drawing()
