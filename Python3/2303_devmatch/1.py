def solution(block):
    n = len(block)
    m = sum(block[0])
    walls = []


    blocks = [[] for _ in range(n * m)]  # blocks[i] := i 번 블록에 포함된 좌표

    cnt = 0
    for i, line in enumerate(block):
        wall_line = []

        j = 0
        for col in line:
            cnt += 1
            for _ in range(col):
                wall_line.append(cnt)
                blocks[cnt].append((i, j))
                j += 1

        walls.append(wall_line)

    max_cnt = -1
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

    for target_num in range(1, cnt + 1):

        mem = set()
        for i, j in blocks[target_num]:
            for di, dj, in dirs:
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < m):
                    continue
                mem.add(walls[ni][nj])

        if target_num in mem:
            mem.remove(target_num)
        if max_cnt < len(mem):
            max_cnt = len(mem)

    return max_cnt


print(solution([[3, 1, 1, 2], [2, 3, 2], [1, 1, 2, 3]]))
