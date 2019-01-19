class Graph(object):
    def __init__(self, start, end, graph):
        self.graph = self.__parse_graph__(graph)
        self.start = start
        self.end = end
        self.solutions = []

    def __parse_graph__(self, graph):
        parsed_gr = {}
        for tup in graph:
            parsed_gr[tup[0]] = tup[1]
        return parsed_gr

    def backtrack(self, start, end, path=[]):
        if end in self.graph[start]:
            self.solutions.append(path + [start, end])
            return
        for point in self.graph[start]:
            path.append(start)
            if point not in path:
                self.backtrack(point, end, path)
            path.pop()


def non_overlapping_paths(start, end, graph):
    graph = Graph(start, end, graph)
    graph.backtrack(start, end)
    return graph.solutions
