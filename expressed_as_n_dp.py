"""
https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3#
Programmers 42895 N으로 표현

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5


5

5+5 (+5 -5 *5 //5 5)
5-5
5*5
5//5
55

"""

import pprint


def solution(N, number):
    MAX_COUNT = 8

    value = [[] for _ in range(MAX_COUNT)]

    for i in range(1, MAX_COUNT):
        value[i].append(int(str(N) * i))

        for j in range(1, i):

            for a in value[j]:
                for b in value[i - j]:
                    value[i].append(a + b)
                    value[i].append(a - b)
                    value[i].append(a * b)
                    if b != 0:
                        value[i].append(a // b)

        for v in value:
            print(v)
        print()

        if number in value[i]:
            return i

    return -1


# case 1 ans = 4
N, number = 5, 12

# case 2 ans = -1
# N, number = 5, 31168


# case 3 ans = 3
# N, number = 5, 4


# case 4 ans = 4
N, number = 5, 54

print(solution(N, number))
