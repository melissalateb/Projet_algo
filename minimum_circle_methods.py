# minimum_circle_methods.py

import time
import math
import random
from minimum_circle_classes import Point, Circle, circle_through_three_points, distance, contains

# Fonction du cercle minimum avec la méthode récursive Welzl
def cercle_minimum_welzl(points):
    global execution_time_welzl
    start_time = time.time() * 1000
    result = welzl_minimal_circle(points, [])
    # result = welzl_minimal_circle_iteratif(points)
    # result =  cercle_minimum_welzl_optimiser(points)
    end_time = time.time() * 1000
    execution_time_welzl = end_time - start_time
    print("temps dexecusion %s" % execution_time_welzl)
    return result, execution_time_welzl


def trivial_1(P, R):
    if not P and len(R) == 0:
        return Circle(Point(0, 0), 0)

    D = Circle(Point(0, 0), 0)

    if len(R) == 1:
        D = Circle(R[0], 0)
    elif len(R) == 2:
        cx = (R[0].x + R[1].x) / 2
        cy = (R[0].y + R[1].y) / 2
        d = math.dist([R[0].x, R[0].y], [R[1].x, R[1].y]) / 2
        p = Point(int(cx), int(cy))
        D = Circle(p, int(math.ceil(d)))
    elif len(R) == 3:
        D = circle_through_three_points(R[0], R[1], R[2])

    return D

def welzl_minimal_circle(P, R):
    P1 = P.copy()
    rand = random.Random()

    d = Circle(Point(0, 0), 0)

    if not P1 or len(R) == 3:
        d = trivial_1([], R)
    else:
        pt = P1[rand.randint(0, len(P1) - 1)]
        P1.remove(pt)
        d = welzl_minimal_circle(P1, R)

        if d is not None and not contains(d, pt):
            R.append(pt)
            d = welzl_minimal_circle(P1, R)
            R.remove(pt)

    return d

# // Ajout stackoverflo error pour samedi
#  Notre version optimisé
def cercle_minimum_welzl_optimiser(points):
    def circle(points, r):
        if len(points) == 0 or len(r) == 3:
            return trivial_circle(r)

        p = points[0]
        min_circle = circle(points[1:], r)
        if min_circle is None or not min_circle.contains_point(p):
            min_circle = circle(points[1:], r + [p])

        return min_circle

    def trivial_circle(r):
        if len(r) == 0:
            return Circle(Point(0, 0), 0)
        elif len(r) == 1:
            return Circle(r[0], 0)
        elif len(r) == 2:
            center_x = (r[0].x + r[1].x) / 2
            center_y = (r[0].y + r[1].y) / 2
            radius = math.sqrt((r[0].x - r[1].x)** 2 + (r[0].y - r[1].y)**2 ) / 2
            return Circle(Point(center_x, center_y), radius)
        else:
            return circle_through_three_points(r[0], r[1], r[2])
    return circle(points, [])

def welzl_minimal_circle_iteratif(points):
    P = points.copy()
    rand = random.Random()

    d = Circle(Point(0, 0), 0)
    R = []
    stack = [(P.copy(), R.copy(), d)]

    while stack:
        P, R, d = stack.pop()
        

        if not P or len(R) == 3:
            # Utilisez None pour indiquer que les points sont colinéaires dans le cas trivial
            d = trivial_1([], R)

            if d is None:
                # Gérer le cas de trois points colinéaires d'une manière appropriée
                pass
        else:
            pt = rand.choice(P)
            
            try:
                stack.append((P.copy(), R.copy(), d))
                if d is not None and not contains(d, pt):
                    R.append(pt)
                    stack.append((P.copy(), R.copy(), d))
                    P.remove(pt)
                    R.remove(pt)
            except ZeroDivisionError:
                # Gérer le cas de trois points colinéaires d'une manière appropriée
                pass

    return d

def trivial(points):
    if len(points) == 0:
        return Circle(Point(0, 0), 0)
    elif len(points) == 1:
        return Circle(points[0], 0)
    elif len(points) == 2:
        center = Point((points[0].x + points[1].x) / 2, (points[0].y + points[1].y) / 2)
        radius = distance(center, points[0])
        return Circle(center, radius)
    else:
        return circle_through_three_points(points[0], points[1], points[2])


# La complexité de la méthode récursive Welzl est déterminée par la relation de récurrence suivante :
# T(n) = 2 * T(n - 1) + O(1), où T est la fonction de complexité temporelle, et n est le nombre de points.
# La solution de cette relation de récurrence est exponentielle : T(n) = O(2^n).

# Fonction du cercle minimum avec la méthode naive
def cercle_minimum_naif(points):
    global execution_time_naive
    start_time = time.time() * 1000

    resX, resY, resRadiusSquared = 0.0, 0.0, float('inf')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                p, q, r = points[i], points[j], points[k]

                if (q.x - p.x) * (r.y - p.y) - (q.y - p.y) * (r.x - p.x) == 0:
                    continue
                if p.y == q.y or p.y == r.y:
                    if p.y == q.y:
                        p, r = points[k], points[i]
                    else:
                        p, q = points[j], points[i]

                mX, mY = 0.5 * (p.x + q.x), 0.5 * (p.y + q.y)
                nX, nY = 0.5 * (p.x + r.x), 0.5 * (p.y + r.y)

                alpha1 = (q.x - p.x) / (p.y - q.y)
                beta1 = mY - alpha1 * mX
                alpha2 = (r.x - p.x) / (p.y - r.y)
                beta2 = nY - alpha2 * nX

                # Vérifier si les droites ne sont pas parallèles
                if alpha1 == alpha2:
                    continue

                cX = (beta2 - beta1) / (alpha1 - alpha2)
                cY = alpha1 * cX + beta1
                cRadiusSquared = (p.x - cX) ** 2 + (p.y - cY) ** 2

                if cRadiusSquared >= resRadiusSquared:
                    continue

                all_hit = all((s.x - cX) ** 2 + (s.y - cY) ** 2 <= cRadiusSquared for s in points)
                if all_hit:
                    resX, resY, resRadiusSquared = cX, cY, cRadiusSquared

    end_time = time.time() * 1000
    execution_time_naive = int(round(end_time - start_time))
    return Circle(Point(resX, resY), resRadiusSquared ** 0.5), execution_time_naive
# La complexité de la méthode naïve peut être exprimée comme une fonction cubique :
# T(n) = O(n^3), où T est la fonction de complexité temporelle, et n est le nombre de points.
# Cela découle de la présence de trois boucles imbriquées, chacune dépendant de la taille de l'ensemble de points.
