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
├── cidades.py
├── algoritmo-genetico.py
├── algoritmo-guloso.py
├── algoritmo-vizinho-proximo.py
└── README.md

```

---

### 🚀 Como Começar

Siga estas instruções para configurar e rodar o projeto em sua máquina local.

#### Pré-requisitos

Você precisa ter o Python 3 e o `pip` instalados em sua máquina.

#### Instalação

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/BrenoCupertino/MATA53-Projeto-Final.git
    ```
2.  **Instale as seguintes dependências**:
    ```bash
    pip install numpy tsplib95 matplotlib
    ```

---

### ▶️ Como Executar

Cada algoritmo é executado a partir de seu próprio arquivo Python.

**⚠️ Importante:** Antes de executar, você precisa escolher qual dataset será usado. Abra o arquivo `cidades.py` e altere a variável `caminho` para o arquivo desejado:

```python
# Exemplo de como configurar para usar o dataset de 76 cidades
caminho = "./data/eil76.tsp.gz"
```
Após configurar o dataset, execute um dos seguintes comandos no seu terminal:
* Para executar o Algoritmo Genético
```python
python algoritmo-genetico.py
```

* Para executar o Algoritmo Guloso:
```python
python algoritmo-guloso.py

```
* Para executar o Algoritmo do Vizinho Mais Próximo:
``` python
python algoritmo-vizinho-proximo.py
```

Ao executar um script, ele irá imprimir no console a melhor rota encontrada, a distância total e o tempo de execução. Em seguida, uma janela do `matplotlib` será aberta, exibindo o gráfico da rota.

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

