# minimum_circle_main.py

import matplotlib.pyplot as plt
from minimum_circle_classes import Point, Circle, circle_through_three_points, generate_random_points, point_in_circle, distance, minimal_circle
from minimum_circle_methods import cercle_minimum_welzl, cercle_minimum_naif

execution_time_naive = None
execution_time_welzl = None

# Renvoie la fenêtre, le graph, et l'ensebmle des points et des cercles
def plot_window(points, welzl_circle,naive_circle):
    global execution_time_naive 
    global execution_time_welzl
    
    # Définit la taille de la figure en pixels
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    plot_points(ax, points)
    plot_circle(ax, naive_circle, color='r', label='Naive Circle')
    print(welzl_circle)
    plot_circle(ax, welzl_circle, color='g', label='Welzl Circle')
    # Definit plusieurs labels et text de la figure et de la fenêtre
    ax.set_title(f'Temps d\'exécution naif: {execution_time_naive} ms\nTemps d\'exécution walzl: {execution_time_welzl} ms')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.grid(True)
    ax.set_xlim(0, 800)
    ax.set_ylim(0, 800)
    fig.canvas.draw()
    plt.legend()
    plt.show()
    

# Dessine les points dans l'axe
def plot_points(ax, points):
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    ax.scatter(x_values, y_values, color='b', label='Points')

# Dessine le cercle dans l'axe
def plot_circle(ax, circle, color, label):
    if color == 'r' : 
        linestyle = 'solid'
    else : 
        linestyle = 'dashed'
    if circle:
        circle_patch = plt.Circle((circle.center.x, circle.center.y),
                                circle.radius, fill=False, color=color, linestyle = linestyle, label=label)
        ax.add_patch(circle_patch)

# Recupère les coordonnées des points à partir d'un fichier donnée
def read_points_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            coordinates = line.strip().split()
            if len(coordinates) == 2:
                x, y = map(float, coordinates)
                points.append(Point(x, y))
    return points

# Lance l'execution des points recupérés a partir de 'read_points_from_file'
# Ecrit le resultat des temps d'execution dans le fichier 'fichiers_temps.txt'
def lancer_execution():
    global execution_time_naive 
    global execution_time_welzl
    for i in range(3, 4):  # Boucler de 1 à 200 inclus
        file_path = f'samples/test-{i}.points'
        points = read_points_from_file(file_path)
        naive_circle, execution_time_naive = cercle_minimum_naif(points)
        welzl_circle, execution_time_welzl = cercle_minimum_welzl(points)
        with open('fichiers_temps.txt', 'a') as fichier:
            fichier.write(f"{i}. {execution_time_naive} / {execution_time_welzl}\n")
    plot_window(points, welzl_circle, naive_circle)

def main():
    global execution_time_welzl
    global execution_time_naive
    # num_points = 20
    # points = generate_random_points(num_points)
    # welzl_circle, execution_time_welzl = cercle_minimum_welzl(points)
    # naive_circle, execution_time_naive = cercle_minimum_naif(points)
    # plot_window(points, welzl_circle, naive_circle)
    lancer_execution()


if __name__ == "__main__":
    main()
