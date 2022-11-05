class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getMagnitude(self):
        return(self.x ** 2 + self.y ** 2) ** 0.5
    
    def setMagnitude(self,n):
        mag = self.getMagnitude()
        try:
            self.x = (self.x * n) / mag
            self.y = (self.y * n) / mag
        except:
            pass

    def add(self, v2):
        return vector(self.x + v2.x, self.y + v2.y)

    def addTo(self, v2):
        self.x += v2.x
        self.y += v2.y

    def subtract(self, v2):
        return vector(self.x - v2.x, self.y - v2.y)

    def subtractFrom(self, v2):
        self.x -= v2.x
        self.y -= v2.y

    def multiply(self, n):
        return vector(self.x * n, self.y * n)

    def multiplyBy(self, n):
        self.x *= n
        self.y *= n

    def divide(self, n):
        return vector(self.x / n, self.y / n)

    def divideBy(self, n):
        self.x /= n
        self.y /= n

    def dotProduct(self, v2):
        return self.x * v2.x + self.y * v2.y

    def normalize(self):
        
        try:
            return vector(self.x / (self.x ** 2 + self.y ** 2) ** 0.5, self.y / (self.x ** 2 + self.y ** 2) ** 0.5)
        except:
            return vector(self.x , self.y)