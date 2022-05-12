class Grafo:

    def __init__(self, num_vet=0, num_arestas=0, lista_adj=None, mat_adj=None):
        self.num_vet = num_vet
        self.num_arestas = num_arestas

        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vet)]
        else:
            self.lista_adj = lista_adj

        if mat_adj is None:
            self.mat_adj = [[0 for i in range(num_vet)] for j in range(num_vet)]
        else:
            self.mat_adj = mat_adj

    def addAresta(self, source, destiny, value=1):
        if source < self.num_vet and destiny < self.num_vet:
            self.lista_adj[source].append((destiny, value))
            self.mat_adj[destiny][source] = value
            self.num_arestas += 1
        else:
            print("Aresta Inválida")

    def remove_aresta(self, source, destiny):
        if source < self.num_vet and destiny < self.num_vet:
            if self.mat_adj[source][destiny] != 0:
                self.num_arestas -= 1
                self.mat_adj[source][destiny] = 0
                for (v2, w2) in self.lista_adj[source]:
                    if v2 == destiny:
                        self.lista_adj[source].remove((v2, w2))
                        break
            else:
                print("Aresta inexistente!")
        else:
            print("Aresta invalida!")

    def grau(self, v: int) -> int:
        return len(self.lista_adj[v])

    def regular(self) -> bool:
        aux = self.grau(self.lista_adj)

        for i in range(1, len(self.lista_adj)):
            if self.grau(self.lista_adj, i) != aux:
                return False

        return True

    def completo(self) -> bool:
        for i in range(len(self.lista_adj)):
            if self.grau(self.lista_adj, i) != len(self.lista_adj) - 1:
                return False

        return True

    def ler_arquivo(self, nome_arq):
        try:
            arq = open("dataset/" + nome_arq)
            str = arq.readline()
            str = str.split(" ")
            self.num_vet = int(str[0])
            self.num_arestas = int(str[1])
            print(f"Leitura numero de arestas: {self.num_arestas}")
            self.lista_adj = [[] for i in range(self.num_vet)]
            self.mat_adj = [[0 for i in range(self.num_vet)] for j in range(self.num_vet)]

            for i in range(self.num_arestas):
                str = arq.readline()
                str = str.split(" ")
                source = int(str[0])
                destiny = int(str[1])
                value = int(str[2])
                self.addAresta(source, destiny, value)
        except IOError:
            print("Erro")

    def densidade(self):
        # Calcula a densidade de um grafo num_arestas / num_vet * num_vet-1.
        numeroDeAresta = self.num_arestas
        print(numeroDeAresta)
        numeroVertice = self.num_vet
        print(numeroVertice)
        densidade = self.num_arestas / (self.num_vet * (self.num_vet - 1))

        return float(densidade)

    def subgrafo(self, g2):
        if g2.num_vert > self.num_vet:
            return False
        for i in range(len(g2.mat_adj)):
            for j in range(len(g2.mat_adj[i])):
                if g2.mat_adj[i][j] != 0 and self.mat_adj[i][j] == 0:
                    return False
        return True

    def busca_largura(self, s):
        """Retorna a ordem de descoberta dos vertices pela
           busca em largura a partir de s"""
        desc = [0 for v in range(self.num_vet)]
        Q = [s]
        R = [s]
        desc[s] = 1
        while Q:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        return R

    def busca_profundidade(self, s):
        """Retorna a ordem de descoberta dos vertices pela
           busca em profundidade a partir de s"""
        desc = [0 for v in range(self.num_vet)]
        S = [s]
        R = [s]
        desc[s] = 1
        while S:
            u = S[-1]
            desempilhar = True
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    desempilhar = False
                    S.append(v)
                    R.append(v)
                    desc[v] = 1
                    break
            if desempilhar:
                S.pop(-1)
        return R

    def conexo(self, s):
        """Retorna Ture se o grafo e conexo e False caso contrario
           baseado na busca em largura"""
        desc = [0 for v in range(self.num_vet)]
        Q = [s]
        R = [s]
        desc[s] = 1
        while Q:
            u = Q.pop(0)
            for (v, w) in self.lista_adj[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1
        for i in range(len(desc)):
            if desc[i] == 0:
                return False
        return True

    def ciclo(self, s):
        """Retorna Ture se o grafo tem ciclo e False caso contrario
           baseado na busca em largura"""
        desc = [0 for v in range(self.num_vet)]
        for s in range(self.num_vet):
            if desc[s] == 0:
                Q = [s]
                R = [s]
                desc[s] = 1
                while Q:
                    u = Q.pop(0)
                    for (v, w) in self.lista_adj[u]:
                        if desc[v] == 0:
                            Q.append(v)
                            R.append(v)
                            desc[v] = 1
                        else:
                            return True
        return False

    def caminhoMinimo(self, nome_arq, u, v):
        return
