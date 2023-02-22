import math

def moment_of_inertia(lines):
    # Compute the centroid of the shape
    centroid_x = 0
    centroid_y = 0
    area = 0

    for i in range(len(lines)):
        x1, y1 = lines[i]
        x2, y2 = lines[(i+1)%len(lines)]
        cross_product = x1*y2 - x2*y1
        area += cross_product
        centroid_x += (x1 + x2) * cross_product
        centroid_y += (y1 + y2) * cross_product

    area *= 0.5
    centroid_x /= (6.0*area)
    centroid_y /= (6.0*area)

    # Compute the moment of inertia
    I = 0

    for i in range(len(lines)):
        x1, y1 = lines[i]
        x2, y2 = lines[(i+1)%len(lines)]
        a = x2 - x1
        b = y2 - y1
        length = math.sqrt(a**2 + b**2)
        theta = math.atan2(b, a)
        d = math.sqrt((centroid_x - x1)**2 + (centroid_y - y1)**2)
        I += (length**3) * (math.sin(theta)**2 + math.cos(theta)**2*(d**2)) / 6.0

    return I

# Example usage
lines = [(0, 0), (0, 1), (1, 1), (1, 0)] # A square with side length 1
I = moment_of_inertia(lines)
print("The moment of inertia is:", I)
