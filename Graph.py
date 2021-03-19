import cv2 as cv
from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __call__(self):
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

    def DFSUtil(self, v, visited, img, i, cores):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end='\n')

        i = + 1

        cv.fillPoly(img, pts=[v.get_contorno()], color=(cores[i % 5]))
        cv.imwrite('imagens/iteracao' + str(i) + '.jpg', img)

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in v.adjacent:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, img, i)

        # The function to do DFS traversal. It uses
        # recursive DFSUtil()

    def DFS(self, v):

        img = cv.imread('mapa.jpg')
        copy = img.copy()

        # Create a set to store visited vertices
        visited = set()

        node = self.get_vertex(v)
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(node, visited, copy, i=0)

