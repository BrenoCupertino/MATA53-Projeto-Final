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
