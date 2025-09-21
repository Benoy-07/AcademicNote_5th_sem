G = {
    "A": [("B",20), ("C",30),("D",40)],
    "B": [("E",70), ("F",60)],
    "C": [],  
    "D": [],   
    "E": [],   
    "F": [("G",80), ("H",90)],
    "G": [],  
    "H": [],   
}


H = {
    "A" : 50,
    "B" : 65,
    "C" : 45,
    "D" : 35,
    "E" : 62,
    "F" : 12,
    "G" : 0,
    "H" : 78,
}

from heapq import heappush, heappop

def greedy_best_first(graph, heuristic, start, goal):
    frontier = []
    heappush(frontier, (heuristic[start], 0, start, [start]))
    best_graph = {start: 0}

    while frontier:
        cost, path_cost, node, path_list = heappop(frontier)
        if node == goal:
            return path_cost, path_list
        for neighbor, neighbor_cost in graph[node]:
            updated_cost = cost + heuristic[neighbor]
            if neighbor not in best_graph or updated_cost < best_graph[neighbor]:
                best_graph[neighbor] = updated_cost
                heappush(frontier, (updated_cost, path_cost + neighbor_cost, neighbor, path_list + [neighbor]))

cost, path= greedy_best_first(G, H, "A", "G") 
print("Path : ", " -> ".join(path))
print("Cost : ", cost)