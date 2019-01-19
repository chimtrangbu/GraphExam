def parse_graph(graph):
    parsed_gr = {}
    for tup in graph:
        parsed_gr[tup[0]] = tup[1]
    return parsed_gr


solutions = []


def backtrack(start, end, graph, path=[]):
    if end in graph[start]:
        solutions.append(path + [start, end])
        return
    for point in graph[start]:
        path.append(start)
        if point not in path:
            backtrack(point, end, graph, path)
        path.pop()


def non_overlapping_paths(start, end, graph):
    graph = parse_graph(graph)
    backtrack(start, end, graph)
    return solutions

