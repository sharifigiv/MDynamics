from Body import MDynamics
from Vector import Vector, rotate
from Spring import Spring
import pyray as pr 

# pr.init_window(1080, 720, "Soft Body")

class SoftBody:
    def __init__(self, length: int, particle_column: int, particle_row: int, start_pos: Vector, phy: MDynamics):
        self.length = length
        self.k = 10
        self.damping = 0.4

        self.particle_column = particle_column
        self.particle_row = particle_row

        self.start_pos = start_pos

        self.particles = []
        self.springs = []

        self.phy = phy

    def create_particles(self):
        i = 1
        for row in range(self.particle_row):
            for column in range (self.particle_column):
                particle = self.phy.circle_rigidbody("C" + str(i), row * self.length + self.start_pos.x, column * self.length + self.start_pos.y, 5, 1)
                self.particles.append(particle)
                
                i += 1

    def create_springs(self):
        for i in range(len(self.particles)):
            for j in range(i+1, len(self.particles)):
                length = ((self.particles[i].position.x - self.particles[j].position.x)**2 + (self.particles[i].position.y - self.particles[j].position.y)**2) ** 0.5
                self.springs.append(Spring(self.particles[i], self.particles[j], length, self.k, self.damping))
    
    def update_springs(self):
        for s in self.springs:
            s.update()

    def draw_particles(self):
        for particle in self.particles:
            # print(par)
            pr.draw_circle(int(particle.position.x), int(particle.position.y), particle.r, pr.WHITE)

    def draw_springs(self):
        for spring in self.springs:
            pr.draw_line(int(spring.particle1.position.x), int(spring.particle1.position.y), int(spring.particle2.position.x), int(spring.particle2.position.y), pr.WHITE)

# p = MDynamics()

# s = SoftBody(50, 3, 3, Vector(100, 100), p)
# s.create_particles()
# s.create_springs()

# print(len(s.springs))

# while not pr.window_should_close():
#     pr.begin_drawing()
#     pr.clear_background(pr.BLACK)

#     p.calculate_collisions()
#     p.update_rigid_bodies(0.0009)

#     s.update_springs()

#     s.draw_particles()
#     s.draw_springs()
    

#     pr.end_drawing()
