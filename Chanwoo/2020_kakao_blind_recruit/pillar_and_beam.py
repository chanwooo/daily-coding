"""
[Programmers] 60061 - 기둥과 보

https://programmers.co.kr/learn/courses/30/lessons/60061
2020 카카오 공채 코딩테스트 기출

[x, y, a, b]
x, y : 좌표
a 기둥:0, 보:1
b 삭제:0, 설치:1

기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
"""


def draw(wall):
    for w in wall:
        for e in w:
            if e == 0:
                print(" . ", end="")
            else:
                print('{0:2d}'.format(e), end=" ")
        print()


def solution(n, build_frame):
    n += 1
    wall = [[0] * n for _ in range(n)]

    result = []
    answer = []
    for bf in build_frame:
        x, y, a, b = bf  # x, y, 기둥0보1, 삭제0설치1
        if b == 1:  # 설치
            if a == 0:  # 기둥 설치
                if y == 0 or wall[y][x - 1] >= 2 or wall[y - 1][x] == 1 or wall[y - 1][x] == 3:
                    if not ((wall[y - 1][x - 1] == 1 and wall[y - 1][x - 1] == 1) or (wall[y - 1][x - 1] == 3 and wall[y - 1][x - 1] == 3)):
                        wall[y][x] += 1
                        # result.append([x,y,a])
            else:  # 보 설치
                if wall[y - 1][x] == 1 or wall[y - 1][x] == 3 or wall[y - 1][x + 1] == 0 or (wall[y][x - 1] == 1 and wall[y][x + 1] == 1):
                    wall[y][x] += 2
                    # result.append([x,y,a])
        else: # 삭제
            if a == 0:  # 기둥 삭제
                if wall[y+1][x] != 0 and (wall[y+1][x] + wall[y+1][x-1] != 0):
                    wall[y][x] += -1
                    # result.remove([x, y, a])

            else:  # 보 삭제
                if not (wall[y][x - 1] == 1 and wall[y][x + 1] == 1 and wall[y - 1][x] != 0):
                    wall[y][x] += -2
                    # result.remove([x, y, a])


    for y in range(n):
        for x in range(n):
            if wall[y][x] != -1:
                if wall[y][x]==2:
                    answer.append([x,y,0])
                else:
                    answer.append([x,y,wall[y][x]])


    draw(wall)

    print(sorted(answer))

    # print(sorted(result))
    return sorted(result)


# [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]
# n, bf = 5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

# [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
n, bf = 5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
            [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


# n, bf = 5,[[0,0,0,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[5,1,0,0],[4,2,1,0],[1,0,0,1],[2,0,0,1],[3,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[1,0,0,0],[2,0,0,0],[3,0,0,0]]
# n, bf = 5,[[0,0,0,1],[0,1,0,1],[0,1,1,1],]

print(solution(n, bf))
