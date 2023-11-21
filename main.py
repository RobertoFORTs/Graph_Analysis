#ALUNOS: DANIEL SCHUTZ e ROBERTO FORTES
import random


import random

def criar_grafo(n, p):
    # Dicionário para representar o grafo como um conjunto de adjacência
    grafo = {i: set() for i in range(n)}

    # Loop para criar arestas com probabilidade p entre pares de vértices
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() <= p:
                grafo[u].add(v)
                # Para um grafo não direcionado, precisamos adicionar em ambas direções
                grafo[v].add(u)

    return grafo

def calcular_metricas(grafo):
    num_vertices = len(grafo)
    # Contagem de arestas dividida por 2 para evitar a contagem duplicada em grafos não direcionados
    arestas = sum(len(vizinhos) for vizinhos in grafo.values()) // 2
    graus = [len(vizinhos) for vizinhos in grafo.values()]
    grau_minimo = min(graus)
    grau_maximo = max(graus)
    grau_medio = sum(graus) / num_vertices

    # Algoritmo para encontrar o diâmetro usando busca em largura
    def bfs(start):
        visitados = set()
        fila = [(start, 0)]  # Inicializa a fila com o vértice de início e a distância 0
        max_distancia = 0

        while fila:
            vertice, distancia = fila.pop(0)  # Remove o primeiro elemento da fila
            if vertice not in visitados:
                visitados.add(vertice)
                max_distancia = max(max_distancia, distancia)

                # Adiciona vizinhos não visitados à fila com a distância aumentada em 1
                for vizinho in grafo[vertice]:
                    if vizinho not in visitados:
                        fila.append((vizinho, distancia + 1))

        return max_distancia

    # Calcula o diâmetro como o máximo das distâncias encontradas por BFS a partir de cada vértice
    diametro = max(bfs(v) for v in grafo)

    return num_vertices, arestas, grau_minimo, grau_maximo, grau_medio, diametro


def main():
    inc = int(input("Digite o valor de início (inc): "))
    fim = int(input("Digite o valor final (fim): "))
    stp = int(input("Digite o intervalo entre tamanhos (stp): "))

    # Validando o valor de p
    while True:
        p = float(input(
            "Digite o valor p entre 0 < p ≤ 0.25 indicando a probabilidade de incluir uma aresta no grafo: "))
        if 0 < p <= 0.25:
            break
        else:
            print("O valor de p deve estar no intervalo 0 < p ≤ 0.25. Tente novamente.")

    print("\nProcessando...\n")
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "V", "E", "gmin", "gmax", "gmed", "diam"))
    print("------------------------------------------------------------------------------------")
    for n in range(inc, fim+1, stp):
        grafo = criar_grafo(n, p)
        metricas = calcular_metricas(grafo)
        print("{:<15} {:<15} {:<15} {:<15} {:<15.2f} {:<15.2f}".format(*metricas))


if __name__ == "__main__":
    main()
