
class Edmonds_Karp_algorithm:
    def __init__(self, file):
        self.flow = 0
        self.matrix = self.dataToMatrix(file)
        self.vertex = self.MatrixToVertex()
        self.edges = self.MatrixToEdges()
        self.start = int(input(f"Insert source of the maximum flow from 0 to {len(self.vertex)-1}: "))
        self.end = int(input(f"Insert sink of the maximum flow from 0 to {len(self.vertex)-1} without {self.start}: "))
    def dataToMatrix(self, data):
        number_of_rows = len(data)
        new_data = []
        for x in range(0, number_of_rows):
            new_data.append([int(x) for x in data[x].split(",")])
        return new_data


    def MatrixToVertex(self):
        Vertex = []
        for x,y in enumerate(self.matrix):
            Vertex.append(x)
        return Vertex


    def MatrixToEdges(self):
        Edges = {}
        number_of_rows = len(self.matrix)
        for x,y in enumerate(self.matrix[0]):
            Edges[x] = {}
            for i in range(0, number_of_rows):
                if int(self.matrix[i][x]):
                    Edges[x]["capacity"] = abs(int(int(self.matrix[i][x])))
                    Edges[x]["used_capacity"] = 0
                    Edges[x]["free_capacity"] = abs(int(int(self.matrix[i][x])))
                    if int(self.matrix[i][x]) > 0:
                        Edges[x]["from"] = i
                    elif int(self.matrix[i][x]) < 0:
                        Edges[x]["to"] = i
        return Edges

    def max_flow(self):
        path = self.bfs()
        while path != None:
            flow = min(self.edges[x]["free_capacity"] for x in path)
            for x in path:
                self.edges[x]["free_capacity"] -= flow
                self.edges[x]["used_capacity"] += flow
            path = self.bfs()
        return sum([x["used_capacity"] for x in self.edges.values() if x["to"] == self.end])

    def bfs(self):
        queue = [self.start]
        paths = {self.start: []}
        if self.start == self.end:
            return paths[self.start]
        while queue:
            u = queue.pop(0)
            for y, x in enumerate(self.edges.values()):
                    if x["from"]==u:
                        if x["free_capacity"] > 0 and x["to"] not in paths:
                            paths[x["to"]] = paths[u]+[y]
                            if x["to"] == self.end:
                                return paths[x["to"]]
                            queue.append(x["to"])
        return None

if __name__ == '__main__':
    data = open("graph_init.txt", "r").read().split("\n")
    algorithm = Edmonds_Karp_algorithm(data)
    solve = algorithm.max_flow()
    print(f"Result of maximum flow in this graph is: {solve}")


