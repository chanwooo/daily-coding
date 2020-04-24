"""
[Programmers] 60059 - 자물쇠와 열쇠

https://programmers.co.kr/learn/courses/30/lessons/60059
2020 카카오 공채 코딩테스트 기출
"""


def key_print(key):
    for k in range(len(key)):
        print(key[k])
    print()


def rotate(item):
    N = len(item)
    rotated = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotated[c][N - 1 - r] = item[r][c]
    return rotated


def move(item, i, j):
    N = len(item)
    moved = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):

            if i <= c < N + i and j <= r < N + j:
                moved[r][c] = item[r - j][c - i]
            else:
                moved[r][c] = 0

    return moved


def compare(item1, item2):
    N = len(item1)
    for i in range(N):
        for j in range(N):
            value = item1[i][j] + item2[i][j]
            if value != 1:
                return False
    return True


def solution(key, lock):
    lkey = len(key)
    llock = len(lock)
    N = len(lock)

    for _ in range(llock - lkey):
        for i in range(lkey):
            key[i].append(0)
        key.append([0] * llock)

    keys = []
    keys.append(key)
    # key_print(key)
    for i in range(3):
        keys.append(rotate(keys[i]))
        # key_print(keys[i+1])

    for key in keys:
        for r in range(-N + 1, N):
            for c in range(-N + 1, N):
                # print("move",r,c)
                if compare(move(key, c, r), lock):
                    return True

    return False


k, l = [[1, 0], [0, 1]], [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
print(solution(k, l))
