from math import cos, sin, radians


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getMagnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def setMagnitude(self, n):
        mag = self.getMagnitude()

        try:
            self.x = (self.x * n) / mag
            self.y = (self.y * n) / mag

        except:
            pass

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)

    def __sub__(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def __div__(self, n):
        return Vector(self.x / n, self.y / n)

    def addTo(self, v2):
        self.x += v2.x
        self.y += v2.y

    def subtractFrom(self, v2):
        self.x -= v2.x
        self.y -= v2.y

    def multiply(self, n):
        return Vector(self.x * n, self.y * n)

    def multiplyBy(self, n):
        self.x *= n
        self.y *= n

    def divide(self, n):
        return Vector(self.x / n, self.y / n)

    def divideBy(self, n):
        self.x /= n
        self.y /= n

    def dotProduct(self, v2):
        return self.x * v2.x + self.y * v2.y

    def normalize(self):
        try:
            return Vector(self.x / (self.x ** 2 + self.y ** 2) ** 0.5, self.y / (self.x ** 2 + self.y ** 2) ** 0.5)

        except:
            return Vector(self.x, self.y)


def rotate(origin, point, angle):
    angle = radians(angle)
    ox, oy = origin.x, origin.y
    px, py = point.x, point.y

    qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)

    return Vector(qx, qy)
