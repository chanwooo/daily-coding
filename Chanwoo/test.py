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
#
# print(graph)
#
# def bfs(graph, start_node):
#     visit = list()
#     queue = list()
#     queue.append(start_node)
#
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit.append(node)
#             queue.extend(graph[node])
#             print(queue)
#     return visit
#
# def dfs(graph, start_node):
#     visit = list()
#     stack = list()
#
#     stack.append(start_node)
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit.append(node)
#             # stack.extend(graph[node])
#             stack.extend(reversed(graph[node]))
#     return visit
#
# print(bfs(graph,'A'))
#
# print(dfs(graph,'A'))
#
#
#
# def solution(N, number):
#     arr = [[], [], [], [], [], [], [], [], []]
#     min_count = -1
#
#     for i in range(1, 9):
#         arr[i].append(int(str(N) * i))
#
#         for j in range(1, i):
#             for a in arr[j]:
#                 for b in arr[i - j]:
#                     arr[i].append(a + b)
#                     arr[i].append(a - b)
#                     arr[i].append(a * b)
#                     if b is not 0:
#                         arr[i].append(a // b)
#         print(arr)
#
#
#
#         if number in arr[i]:
#             min_count = i
#             break
#     return min_count, arr
#
# v,arr = solution(5, 12)
#
# for a in arr:
#     print(sorted(list(set(a))))
import heapq

heap = [100, 2, 3, 4, 5, 6, 10]
heapq.heapify(heap)

print(heap)  # [1,2,3,5,7]
print('aaa')

for h in heap:
    print(h)
