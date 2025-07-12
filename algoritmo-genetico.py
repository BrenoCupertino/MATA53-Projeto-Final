from cidades import cidades
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# ==========================
# Parâmetros padrão
TAMANHO_POPULACAO = 250
NUM_GERACOES = 200
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.2
GERACOES_SEM_MELHORA = 50

# ==========================
# Pré-processamento de cidades
nomes_cidades = [nome for nome, _, _ in cidades]
coordenadas_cidades = {nome: (x, y) for nome, x, y in cidades}

# ==========================
# Funções principais

def calcular_distancia(cidade1, cidade2):
    p1, p2 = coordenadas_cidades[cidade1], coordenadas_cidades[cidade2]
    return np.linalg.norm(np.array(p1) - np.array(p2))

def distancia_total(rota):
    return sum(calcular_distancia(rota[i], rota[(i + 1) % len(rota)]) for i in range(len(rota)))

def gerar_populacao_inicial(nomes, tamanho):
    return [random.sample(nomes, len(nomes)) for _ in range(tamanho)]

def calcular_fitness(populacao):
    distancias = np.array([distancia_total(ind) for ind in populacao])
    max_dist = distancias.max()
    pontuacoes = max_dist - distancias
    return pontuacoes / pontuacoes.sum() if pontuacoes.sum() > 0 else np.ones(len(populacao)) / len(populacao)

def selecionar_roleta(populacao, probabilidades):
    acumulado = np.cumsum(probabilidades)
    r = np.random.rand()
    indice = np.searchsorted(acumulado, r)
    return populacao[min(indice, len(populacao) - 1)]

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

# ==========================
# Execução do algoritmo
def executar_ag(tam_pop=TAMANHO_POPULACAO, geracoes=NUM_GERACOES):
    populacao = gerar_populacao_inicial(nomes_cidades, tam_pop)
    melhor_rota, melhor_distancia = min(
        ((ind, distancia_total(ind)) for ind in populacao),
        key=lambda x: x[1]
    )

    sem_melhora = 0

    for _ in range(geracoes):
        fitness = calcular_fitness(populacao)
        nova_populacao = []

        while len(nova_populacao) < tam_pop:
            pai1 = selecionar_roleta(populacao, fitness)
            pai2 = selecionar_roleta(populacao, fitness)
            filho1, filho2 = cruzamento(pai1, pai2)
            nova_populacao.append(mutacao(filho1))
            if len(nova_populacao) < tam_pop:
                nova_populacao.append(mutacao(filho2))

        populacao = nova_populacao
        melhor_atual, dist_atual = min(
            ((ind, distancia_total(ind)) for ind in populacao),
            key=lambda x: x[1]
        )

        if dist_atual < melhor_distancia:
            melhor_rota, melhor_distancia = melhor_atual, dist_atual
            sem_melhora = 0
        else:
            sem_melhora += 1

        if sem_melhora >= GERACOES_SEM_MELHORA:
            print(f"Parou antecipadamente após {geracoes - sem_melhora} gerações.")
            break

    return melhor_rota, melhor_distancia

# ==========================
# Visualização

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

# ==========================
# Execução

if __name__ == "__main__":
    inicio = time.time()
    melhor_rota, melhor_distancia = executar_ag()
    fim = time.time()

    tempo_execucao = fim - inicio
    print("Melhor rota encontrada:", melhor_rota)
    print("Distância total:", melhor_distancia)
    print("Tempo de execução:", round(tempo_execucao, 4), "s")

    exibir_rota(melhor_rota, melhor_distancia, tempo_execucao)
