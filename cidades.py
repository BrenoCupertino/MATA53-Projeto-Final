import tsplib95
import gzip

caminho = "./data/berlin52.tsp.gz"

# Abre o arquivo .gz no modo texto e carrega o conteúdo como string
with gzip.open(caminho, 'rt', encoding='utf-8') as f:
    content = f.read()

# Usa tsplib95.parse() ao invés de load()
problem = tsplib95.parse(content)

# Extrai os nós e coordenadas (caso esteja em formato EUC_2D)
if problem.node_coords:
    cidades = [
        (str(node), x, y) for node, (x, y) in problem.node_coords.items()
    ]
    print("Cidades e suas coordenadas:", cidades)
else:
    raise ValueError("Este problema não possui coordenadas 2D. Verifique o formato.")