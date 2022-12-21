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
