
__date__="19 11 2016 04:45:55"
__Author__="Abdelmajid"
import math
import heapq
import sys


#=====================Implementation d Dijkstra
class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} 
        previous = {}  
        nodes = [] 

        for vertex in self.vertices:
            if vertex == start: 
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        while nodes:
            smallest = heapq.heappop(nodes)[1] 
            if smallest == finish: #
                path = []
                while previous[smallest]: #  
                    path.append(smallest)
                    smallest = previous[smallest]
                parcs=[]#ajouter par AMH
                path.append(start)
                lnn=len(path)
                for i in range(1,lnn):
                    parcs.append(self.vertices[path[i-1]][path[i]])
                    
                return path,parcs
            if distances[smallest] == sys.maxsize: # 
                break
            
            for neighbor in self.vertices[smallest]: # 
                alt = distances[smallest] + self.vertices[smallest][neighbor] # 
                if alt < distances[neighbor]: #  
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)


#=====================Implementation d probleme de premier chemin


def ispremier(n):
	n=math.fabs(n)
	if n<3:return True
	if n%2==0:return False
	m=int(n/2)
	for i in range(3,m+1,2):#diviser seulement sur les nombres impaires
		if n%i==0:
			return False
	return True

##def isSucces(nm1,nm2):
##        """Methde qui verifier si la difference entre deux nombres
##        est un seul chiffre"""
##        reu=set(str(nm1))|set(str(nm2))
##        return True if len(reu)==5 else False

def get_succes(num):
        """Methode qui retourne les nombre qui suivent 'num' """
        suives={}
        m,c,d,u=list(str(num))
        mi,ci,di,ui=int(m),int(c),int(d),int(u)
        for i in [1,3,7,9]:
                if i!=ui:
                        nm=int(m+c+d+str(i))
                        if ispremier(nm):
                                suives[nm]=1
        for i in range(0,10):
                if i!=di:
                        nm=int(m+c+str(i)+u)
                        if ispremier(nm):
                                suives[nm]=1
        for i in range(0,10):
                if i!=ci:
                        nm=int(m+str(i)+d+u)
                        if ispremier(nm):
                                suives[nm]=1
        for i in range(1,10):
                if i!=mi:
                        nm=int(str(i)+c+d+u)
                        if ispremier(nm):
                                suives[nm]=1
        return suives

def contruct_graph(num1):
        """Remplir un graphe des chemins premiers"""
        global g #Graph
        suives=get_succes(num1)
        g.add_vertex(num1, suives)
        news_num=set(suives)
        while len(news_num)>0:
                suiset=set()
                for v in news_num:
                        suives=get_succes(v)
                        g.add_vertex(v, suives)
                        suiset=suiset|set(suives.keys())
                news_num=suiset-set(g.vertices.keys())
                
                
        
        
        
        
        

#============================main==============

if __name__ == '__main__':
    #Watcha !! :)
    g = Graph()
    contruct_graph(1000)#remplir de 1000 jusq 9999 
    #### Goooooooooooo
    n=int(input())
    while n>0:
        n-=1
        num1,num2=str(input()).split(" ")
        num1,num2=int(num1),int(num2)
        nm=g.shortest_path(num1, num2)
        #print(nm)# afficher le chemin s'il exite sinon la matrice de dijkstra
        nm= len(nm[0])-1 if type(nm) is tuple else 0
        print(nm)
        
# si il ya des chemins, on retourne (efges,ditances chemin): ([Fin,E1,E2,start],[Fin-E1,E1-E2,E2-start])
# si il ya plusieurs chemins de minimum couts, il retourne 1 chemin
# si il m ya aucun chemin, on retourne le dictionnaire des distances
