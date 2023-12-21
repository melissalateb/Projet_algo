# minimum_circle_classes.py
import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
    def contains_point(self, point):
        return math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2) <= self.radius


def generate_random_points(num_points):
    points = [Point(random.uniform(200, 600), random.uniform(200, 600)) for _ in range(num_points)]
    return points


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def point_in_circle(p, circle):
    return distance(p, circle.center) <= circle.radius


def circle_through_three_points(p1, p2, p3):
    ax, ay = p1.x, p1.y
    bx, by = p2.x, p2.y
    cx, cy = p3.x, p3.y

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax ** 2 + ay ** 2) * (by - cy) + (bx ** 2 + by ** 2) * (cy - ay) + (cx ** 2 + cy ** 2) * (ay - by)) / d
    uy = ((ax ** 2 + ay ** 2) * (cx - bx) + (bx ** 2 + by ** 2) * (ax - cx) + (cx ** 2 + cy ** 2) * (bx - ax)) / d

    center = Point(ux, uy)
    radius = distance(center, p1)

    return Circle(center, radius)


def minimal_circle(points):
    if len(points) == 0:
        return Circle(Point(0, 0), 0)
    elif len(points) == 1:
        return Circle(points[0], 0)

    if len(points) == 2:
        center = Point((points[0].x + points[1].x) / 2, (points[0].y + points[1].y) / 2)
        radius = distance(points[0], points[1]) / 2
        return Circle(center, radius)

    return circle_through_three_points(points[0], points[1], points[2])
