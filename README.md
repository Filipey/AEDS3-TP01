# Problema do caminho mínimo - Algoritmos e Estruturas de dados III

## Participantes
- [Filipe Augusto Santos de Moura (Aluno)](https://github.com/Filipey)
- [Gustavo Estevam Sena (Aluno)](https://github.com/Gultes)
- [George Henrique Godim da Fonseca (Orientador)](https://github.com/georgehgfonseca)

## Objetivos
- Desenvolver a habilidade de programação em algoritmos em grafos.
- Reforçar o aprendizado sobre os algoritmos para o problema do caminho mínimo.
- Avaliar o impacto da complexidade computacional no tempo de execução.

## Sobre
O trabalho consiste em implementar algoritmos para resolver problemas de caminho
mínimo em grafos. O projeto [Grafos](https://github.com/georgehgfonseca/Grafos), disponibilizado no GitHub, deve ser adaptado com
a implementação dos seguintes algoritmos para caminho mínimo: Busca Largura (para
grafos não ponderados), Dijkstra e Bellman-Ford (para grafos com arestas de peso negativo). O
programa irá, dadas as características do grafo de entrada, escolher automaticamente o
algoritmo mais eficiente para resolvê-lo e a melhor estrutura de dados para representá-lo.

## Run 🏃‍♂️

```bash
# Clone este repositório
$ git clone https://github.com/Filipey/AEDS3-TP01.git

# Acesse o diretório do projeto no terminal
$ cd AEDS3-TP01
````

No arquivo main.py, insira os seguintes dados:

```python
# Arquivo no formato DIMACS presente na pasta /dataset
arquivo = input("Informe o nome do arquivo presente em /dataset: ")

# Vértice de origem do grafo
origem = int(input("Informe o vértice de origem: "))

# Vértice de destino do grafo
destino = int(input("Informe o vértice de destino: "))
```
```
Obs: Para executar o teste do Dijkstra com Fila de Prioridades modificar a última linha de grafo.py para:
return self.formatData(nome_arq, u, v, self.dijkstra_fila_prior(u))

Tempo de Complexidade esperado para esse Algoritmo: O(n*log(n))
```

A execução irá retornar no console a seguinte resposta:
```json

{
  "Arquivo de origem": "toy.txt",
  "Origem": 0,
  "Destino": 4,
  "Caminho": [0, 2, 1, 4],
  "Custo": 7,
  "Tempo": 0.003
}
```


## Feito com ❤️



