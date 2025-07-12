from cidades import cidades
import matplotlib.pyplot as plt
import time

def nearest_neighbor_tsp(nodes, graph):
    path = []
    distances = []

    current_city = 'A'
    origin_index = nodes.index(current_city)

    total_cities = len(nodes)
    steps = 0

    inicio = time.time()
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
    fim = time.time()
    
    tempo_execucao = fim - inicio
    custo_total = sum(distances)
    print("Shortest route : ", " -> ".join(path))
    for i, city in enumerate(path):
        print(f"City {city}'s Nearest Neighbor's Distance is {distances[i]}")
    print("total traveled distance: ", sum(distances))
    
    mostrar_rota(path, coords, nodes, custo_total, tempo_execucao)

def euclidean(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def mostrar_rota(rota, coords, nomes, custo_total, tempo_execucao):
    nome_para_coord = dict(zip(nomes, coords))
    x_rota = [nome_para_coord[n][0] for n in rota] + [nome_para_coord[rota[0]][0]]
    y_rota = [nome_para_coord[n][1] for n in rota] + [nome_para_coord[rota[0]][1]]

    plt.figure(figsize=(16, 10))
    plt.plot(x_rota, y_rota, 'go--', linewidth=2.5, label="Rota vizinho mais próximo")

    for i, cidade in enumerate(rota):
        x, y = nome_para_coord[cidade]
        plt.annotate(f"{i+1} - {cidade}", (x, y), fontsize=12)

    plt.title("Melhor rota com Algoritmo Vizinho Mais Próximo - TSP", fontsize=16)
    plt.suptitle(f"Custo Total: {custo_total:.2f} | Tempo: {tempo_execucao:.4f}s", y=0.92)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    nodes = [nome for nome, _, _ in cidades]

    coords = [(x, y) for _, x, y in cidades]

    graph = [
        [euclidean(a, b) for b in coords] for a in coords
    ]
    
    nearest_neighbor_tsp(nodes, graph)
