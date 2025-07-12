from cidades import cidades
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Parâmetros do Algoritmo
TAMANHO_POPULACAO = 250
NUM_GERACOES = 200
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.2

# Coordenadas das Cidades
nomes_cidades = [nome for nome, _, _ in cidades]
coordenadas_cidades = {nome: (x, y) for nome, x, y in cidades}

# Funções Principais
def calcular_distancia(cidade1, cidade2):
    p1, p2 = coordenadas_cidades[cidade1], coordenadas_cidades[cidade2]
    return np.linalg.norm(np.array(p1) - np.array(p2))

def distancia_total(rota):
    return sum(calcular_distancia(rota[i], rota[(i + 1) % len(rota)]) for i in range(len(rota)))

def gerar_populacao_inicial():
    populacao = []
    for _ in range(TAMANHO_POPULACAO):
        rota = nomes_cidades.copy()
        random.shuffle(rota)
        populacao.append(rota)
    return populacao

def selecionar_roleta(populacao, probabilidades):
    acumulado = np.cumsum(probabilidades)
    r = np.random.rand()
    indice = np.searchsorted(acumulado, r)
    return populacao[min(indice, len(populacao) - 1)]

def calcular_fitness(populacao):
    distancias = np.array([distancia_total(ind) for ind in populacao])
    max_dist = distancias.max()
    pontuacoes = max_dist - distancias
    return pontuacoes / pontuacoes.sum() if pontuacoes.sum() != 0 else np.ones(len(populacao)) / len(populacao)

def cruzamento(pai1, pai2):
    corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:corte] + [c for c in pai2 if c not in pai1[:corte]]
    filho2 = pai2[:corte] + [c for c in pai1 if c not in pai2[:corte]]
    return filho1, filho2

def mutacao(rota):
    if random.random() < TAXA_MUTACAO:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]
    return rota

def executar_ag():
    populacao = gerar_populacao_inicial()
    melhor_rota = min(populacao, key=distancia_total)
    melhor_distancia = distancia_total(melhor_rota)

    for _ in range(NUM_GERACOES):
        fitness = calcular_fitness(populacao)
        nova_populacao = []

        pais = [selecionar_roleta(populacao, fitness) for _ in range(int(TAMANHO_POPULACAO * TAXA_CROSSOVER))]

        for i in range(0, len(pais) - 1, 2):
            filho1, filho2 = cruzamento(pais[i], pais[i + 1])
            nova_populacao.append(mutacao(filho1))
            nova_populacao.append(mutacao(filho2))

        populacao += nova_populacao
        populacao.sort(key=distancia_total)
        populacao = populacao[:TAMANHO_POPULACAO]

        melhor_atual = min(populacao, key=distancia_total)
        dist_atual = distancia_total(melhor_atual)
        if dist_atual < melhor_distancia:
            melhor_rota = melhor_atual
            melhor_distancia = dist_atual


    return melhor_rota, melhor_distancia

# Plot do resultado final

def exibir_rota(rota, distancia, tempo_execucao):
    x_rota = [coordenadas_cidades[c][0] for c in rota] + [coordenadas_cidades[rota[0]][0]]
    y_rota = [coordenadas_cidades[c][1] for c in rota] + [coordenadas_cidades[rota[0]][1]]

    plt.figure(figsize=(16, 10))
    plt.plot(x_rota, y_rota, 'go--', label="Melhor rota", linewidth=2.5)

    for i, cidade in enumerate(rota):
        plt.annotate(f"{i+1} - {cidade}", coordenadas_cidades[cidade], fontsize=12)
    
    plt.title("Melhor Rota com Algoritmo Genético - TSP", fontsize=16)
    plt.suptitle(f"Custo Total: {distancia:.2f} | Tempo: {tempo_execucao:.4f}s", y=0.92)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Execução
inicio = time.time()
melhor_rota, melhor_distancia = executar_ag()
fim = time.time()
tempo_execucao = fim - inicio
# Mostrar os resultados
print("Melhor rota encontrada:", melhor_rota)
print("Distância total:", melhor_distancia)

exibir_rota(melhor_rota, melhor_distancia, tempo_execucao)

