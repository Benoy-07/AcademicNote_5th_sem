# from collections import deque
# tree = {
#         'A': ['B', 'E'],
#         'B': ['C', 'D'],
#         'C': ['F'],
#         'D': [],
#         'E': [],
#         'F': []
#     }
# def bfs(tree, start):
#     visited = []
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#             print(node, end=" ")

#             for neighbor in tree[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)

# bfs(tree, 'A')

from collections import deque
tree = {
    'A' : ['B', 'E'],
    'B' : ['C', 'D'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
    }

def bfs(tree, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
            
            for neighbour in tree[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
bfs(tree, 'A')