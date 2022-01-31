def breath_first_search(graph, value):
    queue = [value]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)

            

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

breath_first_search(graph, "a")