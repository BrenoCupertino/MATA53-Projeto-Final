# TSP: Comparativo de Algoritmos para o Problema do Caixeiro Viajante

Projeto final da disciplina MATA53 Teoria dos Grafos, com o objetivo de implementar, analisar e comparar o desempenho de diferentes algoritmos heurísticos e meta-heurísticos na resolução do Problema do Caixeiro Viajante (TSP).

O projeto utiliza diversos datasets da biblioteca TSPLIB para avaliar a eficiência e a qualidade das soluções encontradas por cada abordagem.

---

### 📖 Sobre o Projeto

O Problema do Caixeiro Viajante é um dos problemas de otimização mais famosos da ciência da computação. Dada uma lista de cidades e as distâncias entre cada par delas, o desafio é encontrar a rota mais curta possível que visita cada cidade exatamente uma vez e retorna à cidade original.

Este projeto implementa três abordagens distintas para encontrar soluções aproximadas para o TSP:

1.  **Algoritmo Guloso**
2.  **Algoritmo Genético**
3.  **Algoritmo Vizinho Mais Próximo**

O objetivo é comparar o custo (distância total) da rota encontrada e o tempo de execução de cada algoritmo em diferentes conjuntos de dados, variando em tamanho e complexidade.

---

### 🛠️ Tecnologias Utilizadas

As seguintes ferramentas e bibliotecas foram essenciais para a construção do projeto:

* **Python 3.x**
* **`tsplib95`**: Para fazer o parsing dos arquivos de datasets `.tsp`.
* **`numpy`**: Para cálculos matemáticos e de distância eficientes.
* **`matplotlib`**: Para a visualização gráfica das rotas encontradas.

---

### 📁 Estrutura do Projeto

Para que os scripts funcionem corretamente, a estrutura de pastas deve ser a seguinte:

```
MATA53-Projeto-Final/ 
├── data/
│   ├── berlin52.tsp.gz
│   ├── d198.tsp.gz
│   ├── eil76.tsp.gz
│   ├── kroA100.tsp.gz
│   ├── kroA150.tsp.gz
│   └── pcb442.tsp.gz
├── algoritmos/
│   ├── algoritmo-genetico.py
│   ├── algoritmo-guloso.py
│   ├── algoritmo-vizinho-proximo.py
├── benchmark.py
└── README.md

```

---

### 🚀 Como Começar

Siga estas instruções para configurar e rodar o projeto em sua máquina local.

#### Pré-requisitos

Você precisa ter o Python 3 e o `pip` (que já vem com o Python 3) instalados em sua máquina.

#### Instalação

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/BrenoCupertino/MATA53-Projeto-Final.git
    ```
2.  **Estando dentro da raiz do projeto, instale as seguintes dependências**:
    ```bash
    pip install numpy tsplib95 matplotlib
    ```

---

### ▶️ Como Executar

**⚠️ Importante:** Dado o conjunto de datasets utilizados e as diferenças nos algoritmos o teste pode demorar cerca de 3min para ser finalizado.

Os algoritmos são executados para um conjunto de datasets pré-definidos.

```python
# Exemplo de como configurar para usar o dataset de 76 cidades
caminho = "./data/eil76.tsp.gz"
```
É necessário duas abordagens diferentes para executar o código nos sistemas Linux e Windows.

* Para executar no sistema Windows, execute o comando abaixo na pasta raiz do projeto:
```python
python benchmark.py
```

* Para executar no Linux, execute o comando abaixo na pasta raiz do projeto:
```python
python3 benchmark.py
```

Ao executar o script, será imprimido no console o dataset atual, numero de cidades, custo total e o tempo de execução. Em seguida, uma janela do `matplotlib` será aberta, exibindo um gráfico de comparação dos algoritmos.

### 📊 Datasets Utilizados

O projeto foi testado com os seguintes datasets da TSPLIB:

* berlin52.tsp.gz (52 cidades)
* eil76.tsp.gz (76 cidades)
* kroA100.tsp.gz (100 cidades)
* kroA150.tsp.gz (150 cidades)
* d198.tsp.gz (198 cidades)
* pcb442.tsp.gz (442 cidades)

### 👤 Equipe
* Breno Cupertino
* Bruna Anunciação
* Joab Guimarães

