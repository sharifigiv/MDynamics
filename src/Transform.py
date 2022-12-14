from Vector import Vector


class RigidBody:
    def __init__(self, mass, position, type, sides):
        if type == "polygon":
            self.type = 'polygon'
        self.mass = mass
        # self.area = self.width * self.height

        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.r = (self.mass ** 0.5) * 10
        self.mu = 0.8
        self.dt = 0

    def applyForce(self, force):
        # f = m * a
        # a = f / m

        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

    

    def collision(self, rb):
        # if (rb.position.x + rb.width + (rb.velocity.x * self.dt) >= self.position.x + (self.velocity.x * self.dt) and rb.position.x+(rb.velocity.x * self.dt) <= self.position.x + self.width + (self.velocity.x * self.dt) and rb.position.y + rb.height + (rb.velocity.y * self.dt) >= self.position.y + (self.velocity.y * self.dt) and rb.position.y + (rb.velocity.y * self.dt) <= self.position.y + self.height + (self.velocity.y * self.dt)):

        mv1 = self.velocity.multiply(self.mass)
        mv2 = rb.velocity.multiply(rb.mass)
        mv = mv1.add(mv2)

        deltav = self.velocity.subtract(rb.velocity)
        deltav.multiplyBy(rb.mass)
        deltamv = mv.subtract(deltav)

        v1p = Vector(deltamv.x / (self.mass + rb.mass),
                        deltamv.y / (self.mass + rb.mass))
        v2p = Vector(self.velocity.x + v1p.x - rb.velocity.x,
                        self.velocity.y + v1p.y - rb.velocity.y)

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
        friction = Vector(0, self.mass * 9.81)
        friction.multiplyBy(mu)
        friction.multiplyBy(-1)

        self.applyForce(friction)

    def update(self, dt, edges=True):
        self.dt = dt
        if edges:
            if self.position.y >= 720 - self.height:
                self.position.y = 720 - self.height
                self.friction(self.mu)
                self.velocity.y *= -1

            if self.position.x >= 1080 - self.width:
                self.position.x = 1080 - self.width
                self.friction(self.mu)
                self.velocity.x *= -1

            if self.position.x <= 0:
                self.position.x = 0
                self.friction(self.mu)
                self.velocity.x *= -1

            if self.position.y <= 0:
                self.position.y = 0
                self.friction(self.mu)
                self.velocity.y *= -1

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        self.acceleration = Vector(0, 0)
