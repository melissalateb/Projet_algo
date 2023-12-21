import random
import math
import matplotlib.pyplot as plt

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

    def contains_all_points(self, points):
        return all(self.contains_point(point) for point in points)

    def get_area(self):
        return math.pi * self.radius**2
    
    # def get_radius(self):
    #     return
    # def contains(self, point):
    #     distance = math.sqrt((point.x - self.center[0]) ** 2 + (point[1] - self.center[1]) ** 2)
    #     return distance <= self.radius

def circle_through_three_points(p1, p2, p3):
    # Implémentation pour créer un cercle à partir de trois points
    # Calcul du centre du cercle circonscrit
    d = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
    center_x = ((p1.x**2 + p1.y**2) * (p2.y - p3.y) + (p2.x**2 + p2.y**2) * (p3.y - p1.y) + (p3.x**2 + p3.y**2) * (p1.y - p2.y)) / d
    center_y = ((p1.x**2 + p1.y**2) * (p3.x - p2.x) + (p2.x**2 + p2.y**2) * (p1.x - p3.x) + (p3.x**2 + p3.y**2) * (p2.x - p1.x)) / d

    # Calcul du rayon du cercle circonscrit
    radius = math.sqrt((center_x - p1.x)**2 + (center_y - p1.y)**2)

    return Circle(Point(center_x, center_y), radius)

def circle_with_diameter(p1, p2):
    # Implémentation pour créer un cercle à partir d'un diamètre
    center_x = (p1.x + p2.x) / 2
    center_y = (p1.y + p2.y) / 2
    radius = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2) / 2

    return Circle(Point(center_x, center_y), radius)

def circle_with_three_points(p1, p2, p3):
    # Implémentation pour créer un cercle à partir de trois points
    # Utilisation de la méthode de Welzl
    return circle_through_three_points(p1, p2, p3)

