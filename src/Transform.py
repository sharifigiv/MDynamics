from Vector import *
from Collision import *
from Const import *


class RigidBody:
    def __init__(self, mass, position):
        self.mass = mass

        self.position = position

        self.n_colliders = 0

        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        self.angular_velocity = 0
        self.angular_acceleration = Vector(0, 0)

        self.mu = 0.8

        self.dt = 0

    def applyForce(self, force):
        # f = m * a
        # a = f / m

        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

    def applyAngularForce(self, force, point):
        # a = (F * r) / 2
        self.acceleration.x += force.x / self.mass
        self.acceleration.y += force.y / self.mass

        r = 0
        F = 0

        a = (self.sides[0][1] - self.sides[0][0])
        a = a.getMagnitude()

        I = (a ** 4) / 6

        for line in self.sides:
            if line_point(line[0], line[1], point):
                r = (line[0] + line[1]) / 2
                r = point - r
                r.getMagnitude()

                break

        self.angular_acceleration = (F * r) / I

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


class Classic_Poly(RigidBody):
    def __init__(self, sides, mass, position):
        self.sides = sides
        self.type = 'Poly'
        RigidBody.__init__(self, mass, position)
        sum_x = 0
        sum_y = 0
        points = []

        gaz = (self.sides[0][0].x - self.sides[0][1].x) ** 2 + \
            (self.sides[0][0].y - self.sides[0][1].y) ** 2

        for side in sides:
            if side[0] not in points:
                sum_x += side[0].x

                sum_y += side[0].y
                points.append(side[0])

            if side[1] not in points:
                sum_x += side[1].x
                sum_y += side[1].y
                points.append(side[1])
        self.center = Vector(sum_x/len(points), sum_y/len(points))

    def update(self, dt, edges=True):
        self.dt = dt

        if self.sides[0][0].y >= 720:
            self.friction(self.mu)
            self.velocity.y *= -1

        # if poly_line(self.sides, Vector(0, 0), Vector(1280, 0)):
        #     self.friction(self.mu)
        #     self.velocity.y *= -1

        # if poly_line(self.sides, Vector(1280, 0), Vector(1280, 720)):
        #     self.friction(self.mu)
        #     self.velocity.x *= -1

        # if poly_line(self.sides, Vector(0, 0), Vector(0, 720)):
        #     self.friction(self.mu)
        #     self.velocity.x *= -1

        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        self.sides[0][0].x += self.velocity.x * dt
        self.sides[0][0].y += self.velocity.y * dt

        self.sides[len(self.sides)-1][1].x += self.velocity.x * dt
        self.sides[len(self.sides)-1][1].y += self.velocity.y * dt

        self.angular_velocity += self.angular_acceleration.y * dt
        self.angular_velocity += self.angular_acceleration.x * dt

        for line in self.sides:
            for point in line:
                point.x += self.velocity.x * dt
                point.y += self.velocity.y * dt
        self.center += Vector(self.velocity.x * dt, self.velocity.y * dt)

        for line in self.sides:
            for point in line:
                point2 = rotate(self.center, point, self.angular_velocity)
                line[line.index(point)] = point2

        self.acceleration = Vector(0, 0)
        self.angular_acceleration = Vector(0, 0)

    def collision(self, R2):
        if R2.type == 'Circle':
            if poly_circle(self.sides, R2):
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1 + mv2

                deltav = self.velocity - R2.velocity
                deltav.multiplyBy(R2.mass)
                deltamv = mv - deltav

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                             deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                             self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

        elif R2.type == 'Poly':
            poly1 = self
            poly1.update(poly1.dt)

            poly2 = R2
            poly2.update(poly2.dt)
            collide, final1, final2 = poly_poly(poly2.sides, poly1.sides)
            if collide:
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1 + mv2

                deltav = self.velocity - R2.velocity
                deltav.multiplyBy(R2.mass)
                deltamv = mv - deltav

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                             deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                             self.velocity.y + v1p.y - R2.velocity.y)

                f1 = (v1p - self.velocity).divide(self.mass)
                f2 = (v2p - R2.velocity).divide(R2.mass)

                self.velocity = v1p
                R2.velocity = v2p

                R2.angular_acceleration = Vector(
                    0, (f2 * final2) / R2.inertia * 1000000)
                self.angular_acceleration = Vector(0, (
                    f1 * final1) / self.inertia * 100000)


class Poly(RigidBody):
    def __init__(self, sides, mass, position):
        self.sides = sides
        self.type = 'Poly'

        RigidBody.__init__(self, mass, position)

        sum_x = 0
        sum_y = 0
        points = []

        gaz = 40

        for side in sides:
            if side[0] not in points:
                sum_x += side[0].x

                sum_y += side[0].y
                points.append(side[0])

            if side[1] not in points:
                sum_x += side[1].x
                sum_y += side[1].y
                points.append(side[1])

        self.center = Vector(sum_x/len(points), sum_y/len(points))
        self.inertia = calculate_inertia(self, gaz)

    def update(self, dt, edges=True):
        self.dt = dt

        if self.sides[0][0].y >= 720:
            self.friction(self.mu)
            self.velocity.y *= -1

        # if poly_line(self.sides, Vector(0, 0), Vector(1280, 0)):
        #     self.friction(self.mu)
        #     self.velocity.y *= -1

        # if poly_line(self.sides, Vector(1280, 0), Vector(1280, 720)):
        #     self.friction(self.mu)
        #     self.velocity.x *= -1

        # if poly_line(self.sides, Vector(0, 0), Vector(0, 720)):
        #     self.friction(self.mu)
        #     self.velocity.x *= -1
        self.velocity.x += self.acceleration.x * dt
        self.velocity.y += self.acceleration.y * dt

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        # self.sides[0][0].x += self.velocity.x * dt
        # self.sides[0][0].y += self.velocity.y * dt

        # self.sides[len(self.sides)-1][1].x += self.velocity.x * dt
        # self.sides[len(self.sides)-1][1].y += self.velocity.y * dt

        self.angular_velocity += self.angular_acceleration.y * dt
        for line in self.sides:
            for point in line:
                point2 = rotate(self.center, point, self.angular_velocity)
                line[line.index(point)] = point2
        for line in self.sides:
            for point in line:
                point.x += self.velocity.x * dt
                point.y += self.velocity.y * dt
        self.center += Vector(self.velocity.x * dt, self.velocity.y * dt)

        self.acceleration = Vector(0, 0)
        self.angular_acceleration = Vector(0, 0)

    def collision(self, R2):
        if R2.type == 'Circle':
            if poly_circle(self.sides, R2):
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1 + mv2

                deltav = self.velocity - R2.velocity
                deltav.multiplyBy(R2.mass)
                deltamv = mv - deltav

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                             deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                             self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

        elif R2.type == 'Poly':
            poly1 = self
            poly1.update(poly1.dt)

            poly2 = R2
            poly2.update(poly2.dt)
            collide, final1, final2 = poly_poly(poly2.sides, poly1.sides)
            if collide:
                self.n_colliders += 1

                # print(self.n_colliders)
                print(self.velocity.x, self.velocity.y, '1')
                print(R2.velocity.x, R2.velocity.y, '2')

                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1 + mv2

                deltav = self.velocity - R2.velocity
                deltav.multiplyBy(R2.mass)
                deltamv = mv - deltav

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                             deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                             self.velocity.y + v1p.y - R2.velocity.y)

                f1 = (v1p - self.velocity).divide(self.mass)
                f2 = (v2p - R2.velocity).divide(R2.mass)

                self.velocity = v1p
                R2.velocity = v2p

                R2.angular_acceleration = (f2 * final2).divide(R2.inertia)
                self.angular_acceleration = (f1 * final1).divide(self.inertia)


class Circle(RigidBody):
    def __init__(self, r, mass, position):
        self.r = r
        self.type = 'Circle'
        RigidBody.__init__(self, mass, position)

    def collision(self, R2):
        if R2.type == 'Circle':
            p1 = self.position
            p2 = R2.position

            dx = p1.x - p2.x
            dy = p1.y - p2.y
            dist = (dx**2 + dy**2)**0.5

            if dist <= self.r + R2.r:
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1 + mv2

                deltav = self.velocity - R2.velocity
                deltav.multiplyBy(R2.mass)
                deltamv = mv - deltav

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                             deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                             self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

        elif R2.type == 'Poly':
            if poly_circle(R2.sides, self):
                mv1 = self.velocity.multiply(self.mass)
                mv2 = R2.velocity.multiply(R2.mass)
                mv = mv1 + mv2

                deltav = self.velocity - R2.velocity
                deltav.multiplyBy(R2.mass)
                deltamv = mv - deltav

                v1p = Vector(deltamv.x / (self.mass + R2.mass),
                             deltamv.y / (self.mass + R2.mass))
                v2p = Vector(self.velocity.x + v1p.x - R2.velocity.x,
                             self.velocity.y + v1p.y - R2.velocity.y)

                self.velocity = v1p
                R2.velocity = v2p

    def update(self, dt, edges=True):
        self.dt = dt

        if edges:
            if self.position.y >= 720 - self.r:
                self.position.y = 720 - self.r
                self.friction(self.mu)
                self.velocity.y *= -1

            if self.position.x >= 1080 - self.r:
                self.position.x = 1080 - self.r
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
