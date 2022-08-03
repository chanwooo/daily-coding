"""
[Programmers] - 42585 쇠막대기

https://programmers.co.kr/learn/courses/30/lessons/42585
"""


def solution(arrangement):
    answer = 0
    q = 0
    last = ''
    for a in arrangement:
        if a == '(':
            q += 1
            if last == '(':
                answer += 1

        elif a == ')':
            q -= 1
            if last == '(':
                answer += q

        last = a

        # print(q,a,answer)

    return answer
