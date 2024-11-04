path = {1: [2],
        2: [4],
        3: [],
        4: [10],
        10:[]}


# print path from 1 to 3 dfs
def dfs(start, end, path):
    if start == end:
        return True
    for i in path[start]:
        if dfs(i, end, path):
            return True
    return False


print(dfs(1, 3, path))


# print path from 1 to 3 bfs
def bfs(start, end, path):
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        for i in path[node]:
            queue.append(i)
    return False


print(bfs(1, 3, path))
