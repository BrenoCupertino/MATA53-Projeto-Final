from cidades import cidades
import math
import matplotlib.pyplot as plt
import random
import time

class Cidade:
    """
    Representa uma cidade e suas coordenadas no plano.
    """
    def __init__(self, x, y, nome):
        # Armazena as coordenadas x e y da cidade.
        self.x = x
        self.y = y
        self.nome = nome

    def custo_para_chegar(self, outra_cidade):
        """
        Calcula a distância euclidiana para outra cidade.
        """
        return math.sqrt((self.x - outra_cidade.x)**2 + (self.y - outra_cidade.y)**2)

    def __repr__(self):
        # Define a representação em string de um objeto Cidade.
        return f"({self.nome} {self.x}, {self.y})"

class RotaGulosa:
    """
    Implementa a solução gulosa para o Problema do Caixeiro Viajante (TSP).
    """
    def __init__(self, lista_cidades):
        # Inicializa os atributos necessários para o cálculo da rota.
        self.cidades = lista_cidades
        self.rota = []
        self.visitada = [False] * len(lista_cidades)
        self.custo_total = 0.0

    def definir_rota(self):
        """
        Constrói a rota seguindo a estratégia gulosa de escolher sempre o vizinho mais próximo.
        """
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
            
            # Se encontrou uma cidade, avança para ela.
            if proxima_cidade:
                self.rota.append(proxima_cidade)
                self.visitada[proximo_indice] = True
                cidade_atual = proxima_cidade
                self.custo_total += custo_minimo
                num_visitadas += 1
            else:
                # Interrompe se não houver mais cidades alcançáveis.
                break
        
        # Finaliza o ciclo, calculando o custo de volta ao ponto de partida.
        if len(self.rota) == len(self.cidades):
            custo_retorno = self.rota[-1].custo_para_chegar(self.rota[0])
            self.custo_total += custo_retorno
        else:
            # Marca que a rota não foi concluída com sucesso.
            self.rota = None 
            self.custo_total = -1

    def obter_rota(self):
        """Retorna a rota final."""
        return self.rota

    def obter_custo_total(self):
        """Retorna o custo total da rota."""
        return self.custo_total

def exibir_rota(rota, custo, tempo_execucao):
    x_rota = [cidade.x for cidade in rota] + [rota[0].x]
    y_rota = [cidade.y for cidade in rota] + [rota[0].y]

    plt.figure(figsize=(16, 10))
    plt.plot(x_rota, y_rota, 'go--', linewidth=2.5, label="Rota gulosa")

    for i, cidade in enumerate(rota):
        plt.annotate(f"{i+1} - {cidade.nome}", (cidade.x, cidade.y), fontsize=12)

    plt.title("Melhor Rota com Algoritmo Guloso - TSP", fontsize=16)
    plt.suptitle(f"Custo Total: {custo:.2f} | Tempo: {tempo_execucao:.4f}s", y=0.92)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --- Bloco de Demonstração ---
if __name__ == "__main__":
    # Gera uma lista de cidades para teste.
    lista_de_cidades = [Cidade(x, y, nome) for nome, x, y in cidades]

    print("Problema do Caixeiro Viajante com Algoritmo Guloso")
    print("-" * 50)
    print("Cidades a visitar:")
    for i, cid in enumerate(lista_de_cidades):
        print(f"  Cidade {i+1}: {cid}")
        
    # Executa o algoritmo.
    inicio = time.time()
    solucao_gulosa = RotaGulosa(lista_de_cidades)
    solucao_gulosa.definir_rota()
    fim = time.time()
    tempo_execucao = fim - inicio

    # Exibe os resultados.
    rota_encontrada = solucao_gulosa.obter_rota()
    custo = solucao_gulosa.obter_custo_total()

    print("-" * 50)
    if rota_encontrada:
        print("Rota encontrada (ordem de visita):")
        caminho_formatado = " -> ".join([str(c.x) + "," + str(c.y) for c in rota_encontrada])
        print(f"  [{caminho_formatado} -> Início]")
        print(f"\nCusto total da rota: {custo:.2f}")
        exibir_rota(rota_encontrada, custo, tempo_execucao)
    else:
        print("Não foi possível encontrar uma rota completa.")