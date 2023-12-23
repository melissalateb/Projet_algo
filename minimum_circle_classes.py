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

# Génération des points aléatoirement
def generate_random_points(num_points):
    points = [Point(random.uniform(200, 600), random.uniform(200, 600)) for _ in range(num_points)]
    return points

# Calcul de la distance entre deux points
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Vérifie que le point est inclus dans le cercle
def point_in_circle(p, circle):
    return distance(p, circle.center) <= circle.radius

# Calcule le cercle circonscrit à un triangle défini par trois points
def circle_through_three_points(p1, p2, p3):
    # Extrait les coordonnées des trois points du triangle
    ax, ay = p1.x, p1.y
    bx, by = p2.x, p2.y
    cx, cy = p3.x, p3.y

    # Calcule le dénominateur commun dans les équations des coordonnées du centre du cercle circonscrit
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    
    # Vérifie si les points sont colinéaires
    if d == 0:
        return None
    # Calcule les coordonnées du centre du cercle circonscrit
    ux = ((ax ** 2 + ay ** 2) * (by - cy) + (bx ** 2 + by ** 2) * (cy - ay) + (cx ** 2 + cy ** 2) * (ay - by)) / d
    uy = ((ax ** 2 + ay ** 2) * (cx - bx) + (bx ** 2 + by ** 2) * (ax - cx) + (cx ** 2 + cy ** 2) * (bx - ax)) / d

    # Crée un objet Point représentant le centre du cercle circonscrit
    center = Point(ux, uy)

    # Calcule le rayon du cercle circonscrit en utilisant la distance entre le centre et l'un des points du triangle
    radius = distance(center, p1)

    # Créer un objet Circle avec le centre et le rayon calculés, puis le retourner
    return Circle(center, radius)

# Calcule le cercle circonscrit minimal pour un ensemble de point
def minimal_circle(points):
    # Cas de base : Aucun point, retourner un cercle avec centre (0, 0) et rayon 0
    if len(points) == 0:
        return Circle(Point(0, 0), 0)
    # Cas particulier : Un seul point, retourner un cercle avec ce point comme centre et rayon 0
    elif len(points) == 1:
        return Circle(points[0], 0)
    
    # Cas particulier : Deux points, calculer le cercle avec le milieu comme centre et demi-distance comme rayon
    elif len(points) == 2:
        center = Point((points[0].x + points[1].x) / 2, (points[0].y + points[1].y) / 2)
        radius = distance(points[0], points[1]) / 2
        return Circle(center, radius)
    
    # Cas général : Trois points ou plus, utiliser la méthode circle_through_three_points
    return circle_through_three_points(points[0], points[1], points[2])

def contains(circle, point):
    distance_squared = (point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2
    return distance_squared <= circle.radius ** 2

