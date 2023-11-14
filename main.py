import networkx as nx
import random


def criar_grafo(n, p):
    grafo = nx.Graph()
    vertices = list(range(n))
    grafo.add_nodes_from(vertices)

    for u in vertices:
        for v in vertices:
            if u != v and random.random() <= p:
                grafo.add_edge(u, v)

    return grafo


def calcular_metricas(grafo):
    num_vertices = grafo.number_of_nodes()
    num_arestas = grafo.number_of_edges()
    graus = list(grafo.degree())
    grau_minimo = min(graus, key=lambda x: x[1])[1]
    grau_maximo = max(graus, key=lambda x: x[1])[1]
    grau_medio = sum(dict(grafo.degree()).values()) / num_vertices

    # Verificar se o grafo é conectado
    if nx.is_connected(grafo):
        diametro = nx.diameter(grafo)
    else:
        # Se não for conectado, calcular o diâmetro da maior componente conectada
        componentes_conectadas = list(nx.connected_components(grafo))
        maior_componente = max(componentes_conectadas, key=len)
        grafo_maior_componente = grafo.subgraph(maior_componente)
        diametro = nx.diameter(grafo_maior_componente)

    return num_vertices, num_arestas, grau_minimo, grau_maximo, grau_medio, diametro

def main():
    inc = int(input("Digite o valor de início (inc): "))
    fim = int(input("Digite o valor final (fim): "))
    stp = int(input("Digite o intervalo entre tamanhos (stp): "))
    print("\nProcessando...\n")
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "n", "V", "E", "gmin", "gmax", "gmed", "diam"))
    print("----------------------------------------------------")
    for n in range(inc, fim+1, stp):
        p = 0.25
        grafo = criar_grafo(n, p)
        metricas = calcular_metricas(grafo)

        # print(f"Experimento com {n} vértices:")
        # print(f"Número de vértices: {metricas[0]}")
        # print(f"Número de arestas: {metricas[1]}")
        # print(f"Grau mínimo: {metricas[2]}")
        # print(f"Grau máximo: {metricas[3]}")
        # print(f"Média dos graus: {metricas[4]}")
        # print(f"Diâmetro: {metricas[5]}\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15.2f} {:<15}".format(
            n, metricas[0], metricas[1], metricas[2], metricas[3], metricas[4], metricas[5]))


if __name__ == "__main__":
    # ini = 10
    # fim = 1000
    # stp = 10
    # p = 0.25

    main()
