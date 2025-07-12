import matplotlib.pyplot as plt
import numpy as np
import random

# Parâmetros do Algoritmo
TAMANHO_POPULACAO = 250
NUM_GERACOES = 200
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.2

# Coordenadas das Cidades
coordenadas_x = [0, 3, 6, 7, 15, 10, 16, 5, 8, 1.5]
coordenadas_y = [1, 2, 1, 4.5, -1, 2.5, 11, 6, 9, 12]
nomes_cidades = ["Salvador", "São Paulo", "Rio de Janeiro", "Brasília", "Curitiba",
                             "Manaus", "Belo Horizonte", "Fortaleza", "Recife", "Porto Alegre"]
coordenadas_cidades = dict(zip(nomes_cidades, zip(coordenadas_x, coordenadas_y)))

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

