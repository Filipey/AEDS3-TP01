from grafo import Grafo

grafo = Grafo()
arquivo = input("Informe o nome do arquivo presente em /dataset: ")
origem = int(input("Informe o vértice de origem: "))
destino = int(input("Informe o vértice de destino: "))
print("\nProcessando...")

grafo.caminhoMinimo(arquivo, origem, destino)
