import cv2 as cv
import random

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None
        self.contorno = []


    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_contorno(self):
        return self.contorno

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, contorno):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        new_vertex.contorno = contorno
        return new_vertex


    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def showImg(img):
    cv.imshow('image', img)
    cv.waitKey(500)
    cv.destroyAllWindows()

def adicionarEdges(g):
    g.add_edge('RS', 'SC', 1)
    
    g.add_edge('SC', 'RS', 1)
    g.add_edge('SC', 'PR', 1)
    
    g.add_edge('PR', 'SC', 1)
    g.add_edge('PR', 'SP', 1)
    g.add_edge('PR', 'MS', 1)

    g.add_edge('SP', 'MS', 1)
    g.add_edge('SP', 'PR', 1)
    g.add_edge('SP', 'MG', 1)
    g.add_edge('SP', 'RJ', 1)

    return g

def popularGrafo(nome, pasta, estados, g):
    
    img = cv.imread(nome)
    copy = img.copy()
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 200, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cont = 0
    for i in range(2,len(contours)): 
        if(cv.contourArea(contours[i]) > 1.0):
            print('Contorno {}. Estado: {}'.format(i, estados[cont]))

            #cv.fillPoly(copy, pts = [contours[i]], color=(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
            #cv.imwrite(pasta+'{}'.format(cont)+nome, copy)

            g.add_vertex(estados[cont], contours[i])

            cont += 1

    return g

def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def main():
    f = Graph()
   
    estados = ['RS','SC','PR','RJ','SP','ES','MS','DF','MG','GO','SE','AL','BA','RO','AC','PE','MT','PB','RN','TO','CE','PI','MA','AM','PA','AP','RR']
    pasta = 'mapa.jpg'
    imagem = 'imagens/'
    
    f = popularGrafo(pasta, imagem, estados, f)
    f = adicionarEdges(f)

    for v in f:
        for w in v.get_connections():
            print('(%s , %s)'  % (v.get_id(), w.get_id()))
            
main()