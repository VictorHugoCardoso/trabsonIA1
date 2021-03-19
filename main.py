import cv2 as cv
import time
from Graph import Graph

# 0 - azul, 
# 1 - verde, 
# 2 - vermelho, 
# 3 - amarelo, 
# 4 - rosa,
cores = [[255,0,0], [0,255,0], [0,0,255], [0, 255, 255], [255, 0, 255]]
estados = ['RS','SC','PR','RJ','SP','ES','MS','DF','MG','GO','SE','AL','BA','RO','AC','PE','MT','PB','RN','TO','CE','PI','MA','AM','PA','AP','RR']
imagem = 'mapa'
pasta = 'imagens/'


def showImg(img):
    img = cv.resize(img,(600,600))
    cv.imshow("Brasil", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def addEdges(g):
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
    g.add_edge('MG', 'DF')
    
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
    g.add_edge('BA', 'MA')
    
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
    g.add_edge('MA', 'BA')
    
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
    g.add_edge('RO', 'AC')
    
    g.add_edge('AC', 'AM')
    g.add_edge('AC', 'RO')
    
    g.add_edge('AM', 'AC')
    g.add_edge('AM', 'RO')
    g.add_edge('AM', 'RR')
    g.add_edge('AM', 'PA')
    
    g.add_edge('DF', 'GO')
    g.add_edge('DF', 'MS')
    
    return g

def addVertexs(nome, pasta, g):
    
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

def DFS(imagem, pasta, graph, n):
    node = graph.get_vertex(n)
    i = 0;
    visited = set()

    img = cv.imread(imagem + '.jpg')
    copy = img.copy()

    DFSUtil(imagem, pasta, node, visited, i, copy)

def DFSUtil(imagem, pasta, node, visited, i, copy):
    visited.add(node)
    print(node, end='\n')

    match = 0
    pos = 0
    j = 0
    for cor in cores:
        for neighbour in node.adjacent:
            if cor == neighbour.get_contorno():
                match = 1

        if match == 1:
            match = 0
        else:
            pos = j;
            break
        j += 1

    cv.fillPoly(copy, pts=[node.get_contorno()], color=(cores[j]))
    node.contorno = cores[j]
    cv.imwrite(pasta + 'bfs-' + str(i) + '.jpg', copy)
    showImg(copy)

    for neighbour in node.adjacent:
        if neighbour not in visited:
            i += 1
            DFSUtil(imagem, pasta, neighbour, visited, i, copy)

def BFS(imagem, pasta, graph, n, savesteps, stepbystep):
    
    img = cv.imread(imagem+'.jpg')
    copy = img.copy()
    
    queue = []
    
    # visita o primeiro, e o enfilera
    node = graph.get_vertex(n)
    node.visited = True
    queue.append(node)

    i,j = 0,0

    start = time.time()
    while queue:

        popped = queue.pop(0)
        print ("[{}] - {}".format(j,popped))

        match = 0
        k = 0
        pos = 0
        for cor in cores:
            for neighbour in popped.adjacent:
                if cor == neighbour.get_contorno():
                    match = 1

            if match == 1:
                match = 0
            else:
                pos = k
                break
            k += 1

        cv.fillPoly(copy, pts = [popped.get_contorno()], color=(cores[k]))
        popped.contorno = cores[k]
        if savesteps: cv.imwrite(pasta+'bfs-'+str(i)+'.jpg', copy)    
        if(stepbystep): showImg(copy)

        for x in popped.adjacent:
            j += 1
            if x.visited == False:
                cv.fillPoly(copy, pts = [x.get_contorno()], color=(0, 0, 0))
                
                if(stepbystep): showImg(copy)

                x.visited = True
                queue.append(x)    

        i += 1

    print("\n{} miliseconds".format(time.time() - start))
        
def main():
    g = Graph()
    
    g = addVertexs(imagem, pasta, g)
    g = addEdges(g)
    
    print("\n")
    print(BFS(imagem, pasta, g,'SP', 1, 1))
    #print(DFS(imagem, pasta, g,'SP'))

main()