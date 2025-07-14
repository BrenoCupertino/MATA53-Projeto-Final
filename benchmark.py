import tsplib95
import gzip
import time
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.dirname(__file__))

from algoritmos.algoritmo_vizinho_proximo import nearest_neighbor_tsp, euclidean
import algoritmos.algoritmo_guloso as guloso
import algoritmos.algoritmo_genetico as genetico

datasets = [
    "berlin52",
    "eil76",
    "kroA100",
    "kroA150",
    "d198",
    "pcb442"
]

resultados = {
    "Vizinho": {"tempos": [], "custos": [], "tamanhos": []},
    "Guloso": {"tempos": [], "custos": [], "tamanhos": []},
    "Genético": {"tempos": [], "custos": [], "tamanhos": []},
}

def carregar_cidades_tsplib(nome_dataset):
    caminho = f"./data/{nome_dataset}.tsp.gz"
    with gzip.open(caminho, 'rt', encoding='utf-8') as f:
        content = f.read()
    problem = tsplib95.parse(content)

    if not problem.node_coords:
        raise ValueError(f"{nome_dataset} não possui coordenadas 2D.")
    
    cidades = [(str(node), x, y) for node, (x, y) in problem.node_coords.items()]
    return cidades

# ========= Execução por algoritmo =========
def rodar_algoritmo_vizinho(cidades):
    nodes = [nome for nome, _, _ in cidades]
    coords = [(x, y) for _, x, y in cidades]
    graph = [[euclidean(a, b) for b in coords] for a in coords]

    inicio = time.perf_counter()
    custo = nearest_neighbor_tsp(nodes, graph)
    fim = time.perf_counter()
    return fim - inicio, custo, len(nodes)

def rodar_algoritmo_guloso(cidades):
    lista = [guloso.Cidade(x, y, nome) for nome, x, y in cidades]
    inicio = time.perf_counter()
    r = guloso.RotaGulosa(lista)
    r.definir_rota()
    fim = time.perf_counter()
    return fim - inicio, r.obter_custo_total(), len(lista)

def rodar_algoritmo_genetico(cidades):
    genetico.cidades = cidades
    genetico.nomes_cidades = [nome for nome, _, _ in cidades]
    genetico.coordenadas_cidades = {nome: (x, y) for nome, x, y in cidades}

    inicio = time.perf_counter()
    _, custo = genetico.executar_ag()
    fim = time.perf_counter()
    return fim - inicio, custo, len(cidades)

# ========= Executa benchmark =========
for nome_dataset in datasets:
    print(f"\n📦 Dataset: {nome_dataset}")
    try:
        cidades = carregar_cidades_tsplib(nome_dataset)

        for nome_alg, funcao in {
            "Vizinho": rodar_algoritmo_vizinho,
            "Guloso": rodar_algoritmo_guloso,
            "Genético": rodar_algoritmo_genetico,
        }.items():
            tempo, custo, tamanho = funcao(cidades)
            resultados[nome_alg]["tempos"].append(tempo)
            resultados[nome_alg]["custos"].append(custo)
            resultados[nome_alg]["tamanhos"].append(tamanho)
            print(f"✅ {nome_alg}: {tamanho} cidades | Tempo: {tempo:.4f}s | Custo: {custo:.2f}")

    except Exception as e:
        print(f"❌ Erro com {nome_dataset}: {e}")

cores = {"Vizinho": "blue", "Guloso": "green", "Genético": "red"}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for nome_alg in resultados:
    ax1.plot(resultados[nome_alg]["tamanhos"], resultados[nome_alg]["tempos"],
             'o-', label=nome_alg, color=cores[nome_alg])
ax1.set_title("Tempo de Execução")
ax1.set_xlabel("Número de Cidades")
ax1.set_ylabel("Tempo (s)")
ax1.grid(True)
ax1.legend()

for nome_alg in resultados:
    ax2.plot(resultados[nome_alg]["tamanhos"], resultados[nome_alg]["custos"],
             'o-', label=nome_alg, color=cores[nome_alg])
ax2.set_title("Custo Total da Rota")
ax2.set_xlabel("Número de Cidades")
ax2.set_ylabel("Custo Total")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
