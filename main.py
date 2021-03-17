import cv2 as cv
import random

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        self.visited = False  

        self.contorno = []

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_contorno(self):
        return self.contorno

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

def showImg(img):
    img = cv.resize(img,(600,600))
    cv.imshow("Brasil", img)
    cv.waitKey(0)
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

    
    g.add_edge('MS', 'PR')
    g.add_edge('MS', 'SP')
    g.add_edge('MS', 'GO')
    g.add_edge('MS', 'MT')

    g.add_edge('MG', 'MT')
    g.add_edge('MG', 'GO')
    g.add_edge('MG', 'BA')
    g.add_edge('MG', 'ES')
    g.add_edge('MG', 'RJ')
    
    g.add_edge('ES', 'MG')
    g.add_edge('ES', 'RJ')
    g.add_edge('ES', 'BA')
    
    g.add_edge('RJ', 'SP')
    g.add_edge('RJ', 'MG')
    g.add_edge('RJ', 'ES')
    
    g.add_edge('GO', 'MS')
    g.add_edge('GO', 'MT')
    g.add_edge('GO', 'TO')
    g.add_edge('GO', 'BA')
    g.add_edge('GO', 'MG')
    g.add_edge('GO', 'DF')
    
    g.add_edge('BA', 'MG')
    g.add_edge('BA', 'ES')
    g.add_edge('BA', 'GO')
    g.add_edge('BA', 'TO')
    g.add_edge('BA', 'PI')
    g.add_edge('BA', 'PE')
    g.add_edge('BA', 'AL')
    g.add_edge('BA', 'SE')
    
    g.add_edge('SE', 'BA')
    g.add_edge('SE', 'AL')
    
    g.add_edge('AL', 'SE')
    g.add_edge('AL', 'BA')
    g.add_edge('AL', 'PE')
    
    g.add_edge('PE', 'AL')
    g.add_edge('PE', 'BA')
    g.add_edge('PE', 'PI')
    g.add_edge('PE', 'CE')
    g.add_edge('PE', 'PB')
    
    g.add_edge('PB', 'RN')
    g.add_edge('PB', 'PE')
    g.add_edge('PB', 'CE')
    
    g.add_edge('RN', 'CE')
    g.add_edge('RN', 'PB')
    
    g.add_edge('CE', 'RN')
    g.add_edge('CE', 'PB')
    g.add_edge('CE', 'PE')
    g.add_edge('CE', 'PI')
    
    g.add_edge('PI', 'CE')
    g.add_edge('PI', 'MA')
    g.add_edge('PI', 'BA')
    g.add_edge('PI', 'PE')
    
    g.add_edge('MA', 'PI')
    g.add_edge('MA', 'TO')
    g.add_edge('MA', 'PA')
    
    g.add_edge('TO', 'GO')
    g.add_edge('TO', 'BA')
    g.add_edge('TO', 'MA')
    g.add_edge('TO', 'PA')
    g.add_edge('TO', 'MT')
    
    g.add_edge('MT', 'MS')
    g.add_edge('MT', 'GO')
    g.add_edge('MT', 'TO')
    g.add_edge('MT', 'PA')
    g.add_edge('MT', 'AM')
    g.add_edge('MT', 'RO')
    
    g.add_edge('PA', 'MT')
    g.add_edge('PA', 'TO')
    g.add_edge('PA', 'MA')
    g.add_edge('PA', 'AP')
    g.add_edge('PA', 'RR')
    g.add_edge('PA', 'AM')
    
    g.add_edge('AP', 'PA')
    
    g.add_edge('RR', 'PA')
    g.add_edge('RR', 'AM')
    
    g.add_edge('RO', 'MT')
    g.add_edge('RO', 'AM')
    
    g.add_edge('AC', 'AM')
    
    g.add_edge('AM', 'AC')
    g.add_edge('AM', 'RO')
    g.add_edge('AM', 'RR')
    g.add_edge('AM', 'PA')
    
    g.add_edge('DF', 'GO')

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


def printGrafo(g):
    for v in g:
        for w in v.get_connections():
            print('(%s , %s)'  % (v.get_id(), w.get_id()))


def bfs(imagem, pasta, graph, n):
    # 0 - azul, 1 - verde, 2 - vermelho, 3 - amarelo, 4 - rosa,
    cores = [[255,0,0], [0,255,0], [0,0,255], [0, 255, 255], [255, 0, 255]]
    
    img = cv.imread(imagem+'.jpg')
    copy = img.copy()

    node = graph.get_vertex(n)
    
    # cria uma lista de visitados, e atributo todos FALSO
    visited = [False] * (graph.num_vertices + 1)
    queue = []
    
    # visita o primeiro, e o enfilera
    node.visited = True
    
    queue.append(node)

    i = 0

    while queue:

        popped = queue.pop(0)
        print (popped, end = "\n")

        cv.fillPoly(copy, pts = [popped.get_contorno()], color=(cores[i%5]))
        cv.imwrite(pasta+'iteracao'+str(i)+'.jpg', copy)    

        showImg(copy)

        for x in popped.adjacent:
            if x.visited == False:
                x.visited = True
                queue.append(x)    

        i += 1
def main():
    g = Graph()
   
    estados = ['RS','SC','PR','RJ','SP','ES','MS','DF','MG','GO','SE','AL','BA','RO','AC','PE','MT','PB','RN','TO','CE','PI','MA','AM','PA','AP','RR']
    imagem = 'mapa'
    pasta = 'imagens/'
    
    g = popularGrafo(imagem, pasta, estados, g)
    g = adicionarConexoes(g)

    print(bfs(imagem, pasta, g,'PA'))

main()