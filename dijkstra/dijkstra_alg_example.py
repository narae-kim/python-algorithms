def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        if node not in processed:
            cost = costs[node]
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
    return lowest_cost_node


def dijkstra_alg(graph, starting_point, target):
    if target not in graph:
        raise ValueError("The target is not in the graph.")
    infinity = float("inf")
    # costs table
    costs = {node: infinity for node in graph.keys() if node != starting_point}
    start_costs = {node: weight for node, weight in graph[starting_point].items()}
    costs.update(start_costs)
    # parents table
    parents = {node: starting_point for node in graph[starting_point].keys()}
    processed = set()

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.add(node)
        node = find_lowest_cost_node(costs, processed)
    if costs[target] is not infinity:
        print("The minimum cost from '{}' to '{}' takes {}.".format(starting_point, target, costs[target]))
        node = target
        path = []
        while True:
            path.append(node)
            if node == starting_point:
                break
            node = parents[node]
        print(*reversed(path), sep=" -> ")
    else:
        print("No path found from '{}' to '{}'.".format(starting_point, target))


if __name__ == '__main__':
    simple_graph = {"start": {}, "a": {}, "b": {}, "finish": {}}
    simple_graph["start"]["a"] = 6
    simple_graph["start"]["b"] = 2
    simple_graph["a"]["finish"] = 1
    simple_graph["b"]["a"] = 3
    simple_graph["b"]["finish"] = 5

    dijkstra_alg(simple_graph, "start", "finish")

    trade_graph = {"book": {}, "LP": {}, "poster": {}, "guitar": {}, "drum": {}, "piano": {}}
    trade_graph["book"]["LP"] = 5
    trade_graph["book"]["poster"] = 0
    trade_graph["LP"]["drum"] = 20
    trade_graph["LP"]["guitar"] = 15
    trade_graph["poster"]["drum"] = 35
    trade_graph["poster"]["guitar"] = 30
    trade_graph["guitar"]["piano"] = 20
    trade_graph["drum"]["piano"] = 10

    dijkstra_alg(trade_graph, "book", "piano")
