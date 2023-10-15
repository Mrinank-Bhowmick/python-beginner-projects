import itertools
import time
import numpy as np

def calculate_total_distance(path, cities):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += cities[path[i]][path[i+1]]
    total_distance += cities[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def tsp_bruteforce(cities):
    num_cities = len(cities)
    if num_cities < 2:
        return 0, [0]

    best_distance = float('inf')
    best_path = None

    # Generate all possible permutations of city indices
    all_permutations = itertools.permutations(range(num_cities))

    for path in all_permutations:
        distance = calculate_total_distance(path, cities)
        if distance < best_distance:
            best_distance = distance
            best_path = path

    return best_distance, best_path

def tsp_dynamic_programming(cities):
    num_cities = len(cities)
    if num_cities < 2:
        return 0, [0]

    # Initialize the memoization table
    memo = {}

    def tsp_dp_helper(i, state):
        if (i, state) in memo:
            return memo[(i, state)]

        if state == (1 << num_cities) - 1:
            return cities[i][0]

        min_distance = float('inf')
        next_state = None
        for j in range(num_cities):
            if (state >> j) & 1 == 0:
                new_state = state | (1 << j)
                distance = cities[i][j] + tsp_dp_helper(j, new_state)
                if distance < min_distance:
                    min_distance = distance
                    next_state = new_state

        memo[(i, state)] = (min_distance, next_state)
        return min_distance

    # Find the optimal TSP path
    state = 1  # Binary representation of visited cities
    min_distance = tsp_dp_helper(0, state)

    # Reconstruct the path
    path = [0]
    current_city = 0
    while state != (1 << num_cities) - 1:
        min_distance, next_state = memo[(current_city, state)]
        for j in range(num_cities):
            if (state >> j) & 1 == 0 and next_state == (state | (1 << j)):
                path.append(j)
                state = next_state
                current_city = j
                break

    path.append(0)  # Return to the starting city
    return min_distance, path

def tsp_greedy(cities):
    num_cities = len(cities)
    if num_cities < 2:
        return 0, [0]

    visited = set()
    path = [0]
    total_distance = 0

    while len(visited) < num_cities - 1:
        min_distance = float('inf')
        nearest_city = None
        current_city = path[-1]

        for city in range(num_cities):
            if city != current_city and city not in visited:
                distance = cities[current_city][city]
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city

        path.append(nearest_city)
        visited.add(nearest_city)
        total_distance += min_distance

    # Return to the starting city
    path.append(0)
    total_distance += cities[path[-2]][0]

    return total_distance, path

# Example usage:
cities = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

while True:
    print("Choose a TSP solving method:")
    print("1. Dynamic Programming")
    print("2. Brute Force")
    print("3. Greedy")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        start_time = time.time()
        best_distance, best_path = tsp_dynamic_programming(cities)
        end_time = time.time()
        method_name = "Dynamic Programming"
    elif choice == '2':
        start_time = time.time()
        best_distance, best_path = tsp_bruteforce(cities)
        end_time = time.time()
        method_name = "Brute Force"
    elif choice == '3':
        start_time = time.time()
        best_distance, best_path = tsp_greedy(cities)
        end_time = time.time()
        method_name = "Greedy"
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        continue

    print(f"Best TSP distance using {method_name}: {best_distance}")
    print(f"Best TSP path using {method_name}: {best_path}")
    print(f"Time taken by {method_name}: {end_time - start_time} seconds")