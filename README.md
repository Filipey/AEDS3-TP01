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

No arquivo main.py, edite manualmente as seguintes instruções:

```python
# Troque toy.txt para outro arquivo de teste contido em dataset
grafo.caminhoMinimo("toy.txt")

# Troque os vértices de origem e destino
grafo.caminhoMinimo("toy.txt", 0, 3)
```
A execução irá retornar no console a seguinte resposta:
```json
{
  "Arquivo de origem": "toy.txt",
  "Origem": 0,
  "Destino": 3,
  "Caminho": [0, 1, 2, 3],
  "Custo": 5,
  "Tempo": 0.003
}
```

## Feito com ❤️



