import math
import random

class Cidade:
    def __init__(self, x, y, nome):
        self.x = x
        self.y = y
        self.nome = nome

    def custo_para_chegar(self, outra_cidade):
        return math.sqrt((self.x - outra_cidade.x)**2 + (self.y - outra_cidade.y)**2)

    def __repr__(self):
        return f"({self.nome} {self.x}, {self.y})"

class RotaGulosa:
    def __init__(self, lista_cidades):
        self.cidades = lista_cidades
        self.rota = []
        self.visitada = [False] * len(lista_cidades)
        self.custo_total = 0.0

    def definir_rota(self):
        if not self.cidades:
            return

        # O ponto de partida é escolhido de forma aleatória.
        indice_inicio = random.randrange(len(self.cidades))
        cidade_atual = self.cidades[indice_inicio]

        self.rota.append(cidade_atual)
        self.visitada[indice_inicio] = True
        num_visitadas = 1

        # Percorre as cidades até que todas tenham sido visitadas.
        while num_visitadas < len(self.cidades):
            proxima_cidade = None
            custo_minimo = float('inf')

            # Busca pela cidade mais próxima que ainda não foi visitada.
            for i, cidade in enumerate(self.cidades):
                if not self.visitada[i]:
                    custo = cidade_atual.custo_para_chegar(cidade)
                    if custo < custo_minimo:
                        custo_minimo = custo
                        proxima_cidade = cidade
                        proximo_indice = i
            
            if proxima_cidade:
                self.rota.append(proxima_cidade)
                self.visitada[proximo_indice] = True
                cidade_atual = proxima_cidade
                self.custo_total += custo_minimo
                num_visitadas += 1
            else:
                break
        
        # Finaliza o ciclo, calculando o custo de volta ao ponto de partida.
        if len(self.rota) == len(self.cidades):
            custo_retorno = self.rota[-1].custo_para_chegar(self.rota[0])
            self.custo_total += custo_retorno
        else:
            self.rota = None 
            self.custo_total = -1

    def obter_rota(self):
        return self.rota

    def obter_custo_total(self):
        return self.custo_total