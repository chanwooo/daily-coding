"""
[BOJ] - 1260 DFS와 BFS

https://www.acmicpc.net/problem/1260
"""

"""
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1
"""


# graph = {
#     'A': ['B'],
#     'B': ['A', 'C', 'H'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E', 'G'],
#     'E': ['D', 'F'],
#     'F': ['E'],
#     'G': ['D'],
#     'H': ['B', 'I', 'J', 'M'],
#     'I': ['H'],
#     'J': ['H', 'K'],
#     'K': ['J', 'L'],
#     'L': ['K'],
#     'M': ['H']
# }

# print(graph)


from collections import defaultdict, deque


def dfs(graph, start_node):
    visit = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            # stack.extend(graph[node])
            stack.extend(sorted(graph[node], reverse=True))
            print(stack, visit)
    return visit


def bfs(graph, start_node):
    visit = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(sorted(graph[node]))

            print(queue, visit)
    return visit


node_len, edge_len,start = map(int, input().split(' '))
graph = defaultdict(set)
# graph = [set([]) for _ in range(node_len+1)]
# print(graph)
for i in range(edge_len):
    a,b = map(int, input().split(' '))
    graph[a].add(b)
    graph[b].add(a)


# print(" ".join(dfs(graph, start)))
# print(" ".join(bfs(graph, start)))
print(*dfs(graph, start))
print(*bfs(graph, start))