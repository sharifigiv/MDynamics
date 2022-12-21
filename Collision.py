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
        next = current +  1
        if(next == len(vertices)):
            next = 0

        vc = vertices[current]
        vn = vertices[next]

        if(((vc.y > point.y and vn.y < point.y) or (vc.y < point.y and vn.y > point.y)) and (point.x < (vn.x - vc.x) * (point.y - vc.y) / (vn.y - vc.y) + vc.x)):
            if collision:
                collision = False
            else: 
                collision = True
    
    return collision