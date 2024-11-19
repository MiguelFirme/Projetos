#dicionário do grafo
import heapq
grafo = {
    'Criciúma' : {'Nova Veneza':4, 'Siderópolis':8},
    'Siderópolis' : {'Treviso':7, 'Nova Veneza':11, 'Urussanga':1,'Criciúma':8},
    'Nova Veneza' : {'Lauro Muller':8, 'Siderópolis':11,'Criciúma':4},
    'Lauro Muller' : {'Içara':7, 'Treviso':2, 'Turvo':4},
    'Treviso' : {'Urussanga':6, 'Lauro Muller':2,'Siderópolis':7},
    'Içara' : {'Turvo':14, 'Araranguá':9,'Lauro Muller':7},
    'Turvo' : {'Lauro Muller':4, 'Içara':14, 'Araranguá':10},
    'Ararangua' : {'Turvo':10, 'Içara':9},
    'Urussanga' : {'Treviso':6, 'Siderópolis':1, 'Turvo':2},
}

def dijkstra(grafo, partida, destino):
    distancias = {no: float('inf') for no in grafo}
    distancias[partida] = 0

    fila = [(0, partida)]

    caminho = {partida: None}
    while fila:
        distancia_atual, no_atual = heapq.heappop(fila)

        if no_atual == destino:
            break

        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual +peso

#chat
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
                caminho[vizinho] = no_atual
    
    # Reconstruir o caminho mais curto
    caminho_final = []
    no = destino
    while no is not None:
        caminho_final.append(no)
        no = caminho[no]
    caminho_final.reverse()
    
    return caminho_final, distancias[destino]

# Exemplo de uso
caminho, distancia = dijkstra(grafo, 'Criciúma', 'Urussanga')
print("Caminho mais curto:", caminho)
print("Distância total:", distancia)