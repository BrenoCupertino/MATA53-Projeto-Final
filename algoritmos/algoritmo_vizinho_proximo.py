def nearest_neighbor_tsp(nodes, graph):
    path = []
    distances = []

    current_city = '1'
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
    custo_total = sum(distances)

    return custo_total

def euclidean(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
