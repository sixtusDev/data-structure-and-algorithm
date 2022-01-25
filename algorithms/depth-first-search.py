class DepthFirstSearch:
    def __init__(self, graph, search_value) -> None:
        self.graph = graph
        self.search_value = search_value
        self.stack = [search_value]

    def search(self):
        while len(self.stack) > 0:
            current = self.stack.pop()
            print(current)
            
            for neighbour in self.graph[current]:
                self.stack.append(neighbour)

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

depth_first_search = DepthFirstSearch(graph, "a")
depth_first_search.search()


