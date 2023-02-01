from Vector import Vector


def line_point(line_point1, line_point2, point):
    distance1 = (((line_point1.x - point.x) ** 2) +
                 ((line_point1.y - point.y) ** 2)) ** 0.5

    distance2 = (((line_point2.x - point.x) ** 2) +
                 ((line_point2.y - point.y) ** 2)) ** 0.5
    line_length = (((line_point1.x - line_point2.x) ** 2) +
                   ((line_point1.y - line_point2.y) ** 2)) ** 0.5
    buffer = 0.1
    if (distance1 + distance2 >= line_length - buffer and distance1 + distance2 <= line_length + buffer):
        return True

    return False


def line_line(point1, point2, point3, point4):

    uA = ((point4.x - point3.x) * (point1.y - point3.y) - (point4.y - point3.y) * (point1.x - point3.x)
          ) / (((point4.y - point3.y) * (point2.x - point1.x) - (point4.x - point3.x) * (point2.y - point1.y))+0.0000001)

    uB = ((point2.x - point1.x) * (point1.y - point3.y) - (point2.y - point1.y) * (point1.x - point3.x)) / \
        (((point4.y - point3.y) * (point2.x - point1.x) -
         (point4.x - point3.x) * (point2.y - point1.y))+0.0000001)

    if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
        return True

    else:
        return False


def poly_point(vertices, point):
    collision = False
    next = 0

    for current in range(len(vertices)):
        next = current + 1
        if (next == len(vertices)):
            next = 0

        vc = vertices[current]
        vn = vertices[next]

        if (((vc.y > point.y and vn.y < point.y) or (vc.y < point.y and vn.y > point.y)) and (point.x < (vn.x - vc.x) * (point.y - vc.y) / (vn.y - vc.y) + vc.x)):
            if collision:
                collision = False
            else:
                collision = True

    return collision


def poly_line(vertices, point1, point2):
    next = 0

    for current in range(len(vertices)):
        next = current + 1
        if (next == len(vertices)):
            next = 0

        point3 = vertices[current]
        point4 = vertices[next]

        collide = line_line(point1, point2, point3[0], point3[1])
        if collide:
            return True

    return False


def poly_poly(poly1, poly2):
    next = 0
    for current in range(len(poly1)):
        next = current + 1
        if (next == len(poly1)):
            next = 0

        vc = poly1[current]
        vn = poly1[next]

        collide = poly_line(poly2, vc[0], vc[1])
        if collide:
            return True
    return False

# 
def circle_point(point, circle):
    
    distance = (((point.x - circle.position.x) ** 2) + ((point.x - circle.position.x) ** 2) ) ** 0.5

    if distance <= circle.r:
        return True
    
    return False


def circle_line(point1, point2, circle):
    inside1 = circle_point(point1, circle)
    inside2 = circle_point(point2, circle)
    if inside1 or inside2:
        return True

    dist = Vector(point1.x - point2.x, point1.y - point2.y)

    length = ((dist.x ** 2) + (dist.y ** 2)) ** 0.5

    dot = (((circle.position.x-point1.x)*(point2.x-point1.x)) +
           ((circle.y-point1.y)*(point2.y-point1.y)))

    closestx = point1.x + (dot * (point2.x - point1.x))
    closesty = point1.y + (dot * (point2.y - point1.y))
    closest = Vector(closestx, closesty)

    onSegment = line_point(point1, point2, closest)
    if not onSegment:
        return False

    distX = closest.x - circle.position.x
    distY = closest.y - circle.y
    distance = ((dist.x ** 2) + (dist.y ** 2)) ** 0.5

    if distance <= circle.r:
        return True

    return False


def poly_circle(vertices, circle):
    next = 0
    for current in range(len(vertices)):
        next = current + 1
        if next == len(vertices):
            next = 0
        current_vector = vertices[current]
        next_vector = vertices[next]
        collision = circle_line(current_vector, next_vector, circle)
        if collision:
            return True
        return False
