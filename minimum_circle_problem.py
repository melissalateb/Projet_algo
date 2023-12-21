import time
from minimum_circle_classes import Point, Circle, circle_through_three_points, circle_with_diameter, circle_with_three_points
import random
import math
import matplotlib.pyplot as plt
execution_time= None
def generate_random_points(num_points):
    points = [Point(random.uniform(200, 600), random.uniform(200, 600)) for _ in range(num_points)]
    return points

def naive_minimum_circle(points):
    minimum_circle = None
    min_area = float('inf')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                circle = circle_through_three_points(points[i], points[j], points[k])
                area = circle.get_area()

                if area < min_area and circle.contains_all_points(points):
                    min_area = area
                    minimum_circle = circle
    print( minimum_circle)
    return minimum_circle

def welzl_minimum_circle(points):
    shuffled_points = points.copy()
    random.shuffle(shuffled_points)

    return welzl_min_circle(shuffled_points, [])

def welzl_min_circle(points, boundary):
    if not points or len(boundary) == 3:
        return make_circle_from_boundary(boundary)

    random_point = points.pop(0)
    circle = welzl_min_circle(points.copy(), boundary)

    if circle and circle.contains_point(random_point):
        return circle

    boundary.append(random_point)
    return welzl_min_circle(points, boundary)

def make_circle_from_boundary(boundary):
    if not boundary:
        return None
    elif len(boundary) == 1:
        return Circle(boundary[0], 0)
    elif len(boundary) == 2:
        return circle_with_diameter(boundary[0], boundary[1])
    else:
        return circle_with_three_points(boundary[0], boundary[1], boundary[2])
# def plot_points(points):
#     plt.figure(figsize=(8, 8),dpi=100)

#     x_values = [point.x for point in points]
#     y_values = [point.y for point in points]
#     plt.scatter(x_values, y_values, color='b', label='Points')
#     plt.legend()
#     plt.title('Minimum points Problem')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.grid(True)
#     plt.show()
def plot_window(points,naive_circle):
    global execution_time
    # Définir la taille de la figure en pixels
    fig, ax = plt.subplots(figsize=(5, 5), dpi=100)

    # Centrer les points au milieu de la fenêtre
    # center_x, center_y = 400, 300  # La moitié de la largeur fixe de 800 pixels et de la hauteur fixe de 600 pixels
    plot_points(ax, points)
    plot_circle_naive(ax,naive_circle)
    ax.legend()
    ax.set_title(f'Temps d\'exécution : {execution_time} millisecondes')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)
    ax.set_xlim(0,800)
    ax.set_ylim(0, 800)
    plt.show()
def plot_points(ax, points):
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    ax.scatter(x_values, y_values, color='b', label='Points')

def plot_circle_naive(ax, naive_circle):
    if naive_circle:
        naive_circle_patch = plt.Circle((naive_circle.center.x, naive_circle.center.y),
                                       naive_circle.radius, fill=False, color='r', linestyle='dashed', label='Naive Circle')
        ax.add_patch(naive_circle_patch)

def cercle_minimum_naif(points):
    global execution_time
    start_time = time.time()*1000
    center = None
    radius = float('inf')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                # Forme le cercle circonscrit avec les points i, j, k
                current_circle = circle_through_three_points(points[i], points[j], points[k])

                # Vérifie si tous les autres points sont à l'intérieur du cercle
                tous_les_points_dans_cercle = True
                for l in range(len(points)):
                    if l != i and l != j and l != k:
                        if not current_circle.contains_point(points[l]):
                            tous_les_points_dans_cercle = False
                            break

                # Met à jour le cercle minimum si nécessaire
                if tous_les_points_dans_cercle and current_circle.radius < radius:
                    center = current_circle.center
                    radius = current_circle.radius
    end_time = time.time()*1000  # Enregistre le temps de fin de l'exécution
    execution_time = int(round(end_time - start_time))
    print ("execution_time : %s", execution_time)
    return Circle(center, radius)

  
def plot_circle_welzl(welzl_circle):
    if welzl_circle:
        welzl_circle_patch = plt.Circle((welzl_circle.center.x, welzl_circle.center.y),
                                        welzl_circle.radius, fill=False, color='g', linestyle='dashed', label='Welzl Circle')
        plt.gca().add_patch(welzl_circle_patch)
def main():
    num_points = 250
    points = generate_random_points(num_points)

    naive_circle = cercle_minimum_naif(points)
    # welzl_circle = welzl_minimum_circle(points)

    # plot_points_and_circles(points, naive_circle, welzl_circle)
    plot_window(points,naive_circle)

if __name__ == "__main__":
    main()
