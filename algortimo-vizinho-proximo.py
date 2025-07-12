def nearest_neighbor_tsp(nodes, graph):
    path = []
    distances = []

    current_city = 'A'
    origin_index = nodes.index(current_city)

    total_cities = len(nodes)
    steps = 0

    while steps < total_cities and current_city not in path:
        path.append(current_city)
        curr_idx = nodes.index(current_city)
        closest_dist = None
        next_city = None

        for idx, value in enumerate(graph[curr_idx]):
            candidate = nodes[idx]
            if candidate not in path:
                if closest_dist is None or value < closest_dist:
                    closest_dist = value
                    next_city = candidate

        distances.append(closest_dist)
        current_city = next_city
        steps += 1

    last_idx = nodes.index(path[-1])
    distances[-1] = graph[last_idx][origin_index]

    print("Shortest route : ", " -> ".join(path))
    for i, city in enumerate(path):
        print(f"City {city}'s Nearest Neighbor's Distance is {distances[i]}")
    print("total traveled distance: ", sum(distances))

if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D', 'E']
    graph = [
        [0, 60, 217, 164, 69],
        [60, 0, 290, 201, 79],
        [217, 290, 0, 113, 303],
        [164, 201, 113, 0, 196],
        [69, 79, 303, 196, 0]
    ]
    
    nearest_neighbor_tsp(nodes, graph)
