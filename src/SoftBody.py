from Body import MDynamics
from Vector import Vector, rotate


class SoftBody:
    def __init__(self, length, particle_num, first_position):
        self.particles = []
        self.springs = []

        self.spring_length = length
        self.k = 50
        self.damping = 0.2

        self.particle_num = particle_num
        self.first_position = first_position

    def create_particles(self):
        sides = []
        new_line = [Vector(self.first_position[0], self.first_position[1]),
                    Vector(self.first_position[0] + self.spring_length, self.first_position[1] + 0)]

        sides.append(new_line)
        for side in range(self.particle_num):
            last_point_2 = sides[len(sides) - 1][1]
            last_point_1 = sides[len(sides) - 1][0]

            line_last = last_point_2 - last_point_1
            final_point = line_last + last_point_2

            final_line = rotate(last_point_2, final_point, 1)
            sides.append([last_point_2, final_line])
        for i in range(self.particle_num):
            for j in range(i, self.particle_num + 1):
                pass
