"""
https://programmers.co.kr/learn/courses/30/lessons/42884
[Programmers] 42884 - 과속카메라
"""


def solution(routes):
    routes = sorted(routes)
    position = []

    ans = 0
    camera = 30001

    for r in routes:
        if r[0] <= camera:
            camera = min(r[1], camera)
        else:
            ans += 1
            position.append(camera)
            camera = r[1]
    ans+=1
    position.append(camera)

    print(position)
    return ans


if __name__ == '__main__':
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]] # 2
    # routes = [[1,3]]
    print(solution(routes))

    # more test case
    print(solution([[-2, -1], [1, 2], [-3, 0]]))  # 2
    print(solution([[0, 0]]))  # 1
    print(solution([[0, 1], [0, 1], [1, 2]]))  # 1
    print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))  # 4
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
    print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
    print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
