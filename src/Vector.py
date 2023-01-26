from math import cos, sin

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getMagnitude(self):
        return(self.x ** 2 + self.y ** 2) ** 0.5
    
    def setMagnitude(self, n):
        mag = self.getMagnitude()

        try:
            self.x = (self.x * n) / mag
            self.y = (self.y * n) / mag

        except:
            pass

    def add(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)

    def addTo(self, v2):
        self.x += v2.x
        self.y += v2.y

    def subtract(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

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

def rotate(point1, point2, angel):
    rotated_vector_p1 = point1.multiply(cos(angel))
    rotated_vector_p1.subtractFrom(point2.multiply(sin(angel)))

    rotated_vector_p2 = point1.multiply(sin(angel))
    rotated_vector_p2.addTo(point2.multiply(cos(angel)))

    return [rotated_vector_p1, rotated_vector_p2]

moteghayer = rotate(Vector(0,0), Vector(1,0), 90)
print(moteghayer[1].x, moteghayer[1].y)