from grafo import Grafo
import time

grafo = Grafo()
arquivo = input("Informe o nome do arquivo presente em /dataset: ")
origem = int(input("Informe o vértice de origem: "))
destino = int(input("Informe o vértice de destino: "))
inicio = time.process_time()
print("\nProcessando...")

grafo.caminhoMinimo(arquivo, origem, destino)
fim = time.process_time()
print(f"Tempo: {fim - inicio}s")
