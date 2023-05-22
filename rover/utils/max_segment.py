import math
import itertools

def compute_euclidean_distance(point1, point2):
    return math.dist(point1, point2)

def find_max_segment(points):
    unique_combinations = list(itertools.combinations(points), 2)
    max_distance = 0.0
    for each_entry in unique_combinations:
        distance = compute_euclidean_distance(each_entry)
        if max_distance < distance:
            max_distance = distance
