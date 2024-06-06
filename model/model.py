import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self.grafo=nx.DiGraph()
        self.idMap={}
        self.AllAlbum=DAO.getAllAlbums()
        for a in self.AllAlbum:
            self.idMap[a.AlbumId]=a

    def creaGrafo(self,canzoni):
        self.grafo.clear()
        self.nodi=DAO.getAlbums(canzoni)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges()


    def addEdges(self):
        nodi=list(self.grafo.nodes)
        for n in nodi:
            for v in nodi:
                if n.numCanzoni-v.numCanzoni!=0:
                    if n.numCanzoni>v.numCanzoni:
                        differenza=n.numCanzoni-v.numCanzoni
                        self.grafo.add_edge(n,v,weight=differenza)
                    else:
                        differenza = v.numCanzoni - n.numCanzoni
                        self.grafo.add_edge(v,n,weight=differenza)

    def getNumNodes(self):
        return len(self.grafo.nodes)


    def getNumEdges(self):
        return len(self.grafo.edges)

    def getBilancio(self,nodo):
        entranti=self.grafo.in_edges(nodo)
        pesoE=0
        for arco in entranti:
            pesoE+=self.grafo[arco[0]][nodo]["weight"]

        uscenti=self.grafo.out_edges(nodo)
        pesoU=0
        for arco in uscenti:
            pesoU+=self.grafo[nodo][arco[1]]["weight"]
        return pesoE-pesoU

    def getSuccessori(self,nodo):
        n=self.idMap[nodo]
        successori=self.grafo.successors(n)
        listSuccessori=list(successori)
        lista=[]
        for s in listSuccessori:
            lista.append((s, self.getBilancio(s)))
        lista.sort(key=lambda x: x[1], reverse=True)
        return lista
