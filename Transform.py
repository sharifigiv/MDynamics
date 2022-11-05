from Vector import vector
class RigidBody:
    def __init__(self, mass, width, height, position):
        self.mass = mass
        self.width = width
        self.height = height
        self.area = self.width * self.height

        self.position = position
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

    def applyForce(self, force):
        # f = m * a
        # a = f / m

        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

    def collision(self, rb):
        if self.position[0] + self.width > rb.position[0] and self.position[0] < rb.position[0] + rb.width and self.position[1] + self.height > rb.position[1] and self.position[1] < rb.position[1] + rb.height:
            # Collision
            mv1 = self.velocity.multiply(self.mass)
            mv2 = rb.velocity.multiply(rb.mass) 
            mv = mv1.add(mv2)

            deltav = self.velocity.subtract(rb.velocity)
            deltav.multiplyBy(rb.mass)
            deltamv = mv.subtract(deltav)

            v1p = vector(deltamv.x / (self.mass + rb.mass), deltamv.y / (self.mass + rb.mass))
            v2p = vector(self.velocity.x + v1p.x - rb.velocity.x , self.velocity.y + v1p.y - rb.velocity.y)

            self.velocity = v1p
            rb.velocity = v2p 

    def drag(self,c):
        drag_direction = self.velocity
        drag_direction.multiply(-1)
        drag_direction = drag_direction.normalize()

        speedSq = drag_direction.getMagnitude()
        drag_direction.setMagnitude(c * speedSq * -1)

        self.applyForce(drag_direction)


    def update(self, dt, edges=True):
        if edges == True:
            if self.position[1] >= 720 - self.height:
                self.position[1] = 720 - self.height
                self.velocity.y *= -1

            if self.position[0] >= 1080 - self.width:
                self.position[0] = 1080 - self.width
                self.velocity.x *= -1

            if self.position[0] <= 0:
                self.position[0] = 0
                self.velocity.x *= -1
            
            if self.position[1] <= 0:
                self.position[1] = 0
                self.velocity.y *= -1

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position[0] += self.velocity.x * dt
        self.position[1] += self.velocity.y * dt

        self.acceleration = vector(0, 0)

# def collision(self, rb):
#     if (self.position[0] + self.width > rb.position[0] and self.position[0] < rb.position[0] + rb.width and self.position[1] + self.height > rb.position[1] and self.position[1] < rb.position[1] + rb.height):
#         # Collision
#         dx = rb.position[0] - self.position[0]
#         dy = rb.position[1] - self.position[1]

#         angle = (math.atan2(dy, dx) * 180) / math.pi
#         if angle < 0:
#             angle += 360

#         if (angle >= 0 and angle < 45) or (angle > 315 and angle < 360):
#             if self.velocity[0] > 0:
#                 self.velocity[0] *= -1
#             if rb.velocity[0] < 0:
#                 rb.velocity[0] *= -1

#         elif angle >= 45 and angle < 135:
#             if self.velocity[1] > 0:
#                 self.velocity[1] *= -1
#             if rb.velocity[1] < 0:
#                 rb.velocity[1] *= -1

#         elif angle >= 135 and angle < 225:
#             if self.velocity[0] < 0:
#                 self.velocity[0] *= -1
#             if rb.velocity[0] > 0:
#                 rb.velocity[0] *= -1

#         else:
#             if self.velocity[1] < 0:
#                 self.velocity[1] *= -1
#             if rb.velocity[1] > 0:
#                 rb.velocity[1] *= -1
