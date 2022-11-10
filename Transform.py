from Vector import Vector

class RigidBody:
    def __init__(self, mass, width, height, position):
        self.mass = mass
        self.width = width
        self.height = height
        self.area = self.width * self.height

        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.r = (self.mass ** 0.5) * 10
    def applyForce(self, force):
        # f = m * a
        # a = f / m

        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

    def collision(self, rb):
        if self.position.x + self.width > rb.position.x and self.position.x < rb.position.x + rb.width and self.position.y + self.height > rb.position.y and self.position.y < rb.position.y + rb.height:
            # Collision
            mv1 = self.velocity.multiply(self.mass)
            mv2 = rb.velocity.multiply(rb.mass) 
            mv = mv1.add(mv2)

            deltav = self.velocity.subtract(rb.velocity)
            deltav.multiplyBy(rb.mass)
            deltamv = mv.subtract(deltav)

            v1p = Vector(deltamv.x / (self.mass + rb.mass), deltamv.y / (self.mass + rb.mass))
            v2p = Vector(self.velocity.x + v1p.x - rb.velocity.x, self.velocity.y + v1p.y - rb.velocity.y)

            self.velocity = v1p
            rb.velocity = v2p

    def drag(self, c):
        drag_direction = self.velocity
        drag_direction.multiply(-1)
        drag_direction = drag_direction.normalize()

        speed_sq = drag_direction.getMagnitude()
        drag_direction.setMagnitude(c * speed_sq * -1)

        self.applyForce(drag_direction)

    def friction(self, mu):
        mu = 0.1
        friction = self.velocity
        friction.multiplyBy(mu)
        friction.multiplyBy(-1)
        friction.multiplyBy(self.mass * 9.8)

        self.applyForce(friction)

    def update(self, dt, edges=True):
        if edges:
            if self.position.y >= 720 - self.height:
                self.position.y = 720 - self.height
                self.velocity.y *= -1
                self.friction(-1)

            if self.position.x >= 1080 - self.width:
                self.position.x = 1080 - self.width
                self.velocity.x *= -1
                self.friction(-1)

            if self.position.x <= 0:
                self.position.x = 0
                self.velocity.x *= -1
                self.friction(-1)
            
            if self.position.y <= 0:
                self.position.y = 0
                self.velocity.y *= -1
                self.friction(-1)

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        self.acceleration = Vector(0, 0)
