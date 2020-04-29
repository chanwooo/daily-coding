from itertools import permutations


def solution(n, weak, dist):
    """
    :param n: 외벽
    :param weak: 취약지점
    :param dist: 친구들 이동 가능 거리
    :return: 친구들 수
    """

    weak_length = len(weak)
    dist_length = len(dist)
    answer = 10  # dist 범위가 1~8 이라 10으로 세팅

    # n 외벽 만큼 다 더해줌
    for i in range(weak_length):
        weak.append(weak[i] + n)

    for i in range(weak_length):
        start_point = list()
        for j in range(i, weak_length + i):
            start_point.append(weak[j])
        # print(start_point)

        perm = permutations(dist, dist_length)

        for p in perm:
            idx = 0
            count = 1
            check_range = start_point[0] + p[idx]

            for k in range(weak_length):
                if start_point[k] > check_range:
                    count += 1
                    if count > len(p):
                        break
                    idx += 1
                    check_range = p[idx] + start_point[k]
            answer = min(answer, count)

    if answer > dist_length:
        return -1

    return answer