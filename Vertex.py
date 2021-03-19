class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        self.visited = False

        self.contorno = []

    def __call__(self,node):
        self.__init__(self,node)

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

