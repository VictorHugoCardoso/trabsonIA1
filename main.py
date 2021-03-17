import cv2 as cv
import random

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        self.visited = False  

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

    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to])
        self.vert_dict[to].add_neighbor(self.vert_dict[frm])

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

def adicionarConexoes(g):
    g.add_edge('RS', 'SC')
    
    g.add_edge('SC', 'RS')
    g.add_edge('SC', 'PR')
    
    g.add_edge('PR', 'SC')
    g.add_edge('PR', 'SP')
    g.add_edge('PR', 'MS')

    g.add_edge('SP', 'MS')
    g.add_edge('SP', 'PR')
    g.add_edge('SP', 'MG')
    g.add_edge('SP', 'RJ')

    return g

def popularGrafo(nome, pasta, estados, g):
    
    img = cv.imread(nome+'.jpg')
    copy = img.copy()
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 200, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cont = 0
    for i in range(2,len(contours)): 
        if(cv.contourArea(contours[i]) > 1.0):
            print('Contorno {}. Estado: {}'.format(i, estados[cont]))
            g.add_vertex(estados[cont], contours[i])

            cont += 1

    return g

def pintarNode(imagem, pasta, g, edge, color):
    img = cv.imread(imagem+'.jpg')
    copy = img.copy()
    
    v = g.get_vertex(edge)

    cv.fillPoly(copy, pts = [v.get_contorno()], color=(color[0], color[1], color[2]))
    cv.imwrite(pasta+imagem+v.get_id()+'.jpg', copy)

def printGrafo(g):
    for v in g:
        for w in v.get_connections():
            print('(%s , %s)'  % (v.get_id(), w.get_id()))

def main():
    g = Graph()
   
    estados = ['RS','SC','PR','RJ','SP','ES','MS','DF','MG','GO','SE','AL','BA','RO','AC','PE','MT','PB','RN','TO','CE','PI','MA','AM','PA','AP','RR']
    imagem = 'mapa'
    pasta = 'imagens/'
    
    g = popularGrafo(imagem, pasta, estados, g)
    g = adicionarConexoes(g)

    pintarNode(imagem, pasta, g, 'PR', [random.randint(1, 255),random.randint(1, 255), random.randint(1, 255)])
    print(printGrafo(g))

main()