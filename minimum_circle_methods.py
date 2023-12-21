# minimum_circle_methods.py

import time
import math
from minimum_circle_classes import Point, Circle, circle_through_three_points

# Fonction du cercle minimum avec la méthode récursive Welzl
def cercle_minimum_welzl(points):
    global execution_time_walzl
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
    start_time = time.time() * 1000
    result = circle(points, [])
    end_time = time.time() * 1000
    execution_time_walzl = end_time - start_time
    return result, execution_time_walzl

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
