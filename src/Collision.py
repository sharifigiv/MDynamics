from Vector import Vector


def line_line(point1, point2, point3, point4):
    uA = ((point4.x - point3.x) * (point1.y - point3.y) - (point4.y - point3.y) * (point1.x - point3.x)
          ) / ((point4.y - point3.y) * (point2.x - point1.x) - (point4.x - point3.x) * (point2.y - point1.y))

    uB = ((point2.x - point1.x) * (point1.y - point3.y) - (point2.y - point1.y) * (point1.x - point3.x)) / \
        ((point4.y - point3.y) * (point2.x - point1.x) -
         (point4.x - point3.x) * (point2.y - point1.y))

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

        collide = line_line(point1, point2, point3, point4)
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

        collide = poly_line(poly2, vc.x, vc.y, vn.x, vn.y)
        if collide:
            return True

    return False