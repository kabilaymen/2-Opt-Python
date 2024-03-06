import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np


def import_excel():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Sélectionnez le fichier Excel",
                                           filetypes=[("Fichiers Excel", "*.xls;*.xlsx")])

    if file_path:
        try:
            df = pd.read_excel(file_path, header=None)  # Retiré index_col=0
            return df.values
        except Exception as e:
            print("Erreur lors de l'importation du fichier Excel :", e)
            return None
    else:
        return None


def two_opt_swap(route, i, k):
    new_route = route[:i] + route[i:k + 1][::-1] + route[k + 1:]
    return new_route


def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i] - 1][route[i + 1] - 1]
    return total_distance


def two_opt_algorithm(distance_matrix):
    num_cities = len(distance_matrix)
    best_route = list(range(1, num_cities + 1))  # Indices commencent à 1
    improvement = True

    while improvement:
        improvement = False
        for i in range(1, num_cities - 1):
            for k in range(i + 1, num_cities):
                new_route = two_opt_swap(best_route, i, k)
                current_distance = calculate_distance(best_route, distance_matrix)
                new_distance = calculate_distance(new_route, distance_matrix)

                if new_distance < current_distance:
                    best_route = new_route
                    improvement = True

    return best_route


def main():
    num_cities = int(input("Combien de villes y a-t-il ? "))

    distance_matrix = import_excel()

    if distance_matrix is None:
        print("Erreur lors de l'importation de la matrice des distances.")
        return
    elif len(distance_matrix) != num_cities or len(distance_matrix[0]) != num_cities:
        print("Erreur : La taille de la matrice des distances ne correspond pas au nombre de villes spécifié.")
        return

    try:
        best_route = two_opt_algorithm(distance_matrix)
        print("Le meilleur chemin trouvé est :", best_route)
        total_distance = calculate_distance(best_route, distance_matrix)
        print("La distance totale du chemin est :", total_distance)
    except Exception as e:
        print("Erreur lors de l'exécution de l'algorithme des 2-échanges :", e)


if __name__ == "__main__":
    main()
