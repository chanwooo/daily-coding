from itertools import permutations


def solution(k, dun):
    answer = 0

    for i in range(1, len(dun) + 1):
        print()

        print(list(permutations(dun, i)))
        for d in permutations(dun, i):

            count = 0
            hp = k

            for e in d:
                if hp >= e[0]:
                    hp -= e[1]
                    count += 1
                    answer = max(answer, count)
                print(hp, e, count)

    print(answer)
    return answer

solution(80, [[80,20],[50,40],[30,10]])