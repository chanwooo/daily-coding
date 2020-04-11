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

from collections import deque


def get_value(expr: str) -> int:
    operations = ['+', '-', '*', '/']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    op_flag = True

    numbers = []
    opers = []
    value = 0

    for c in expr:
        if c in operations:
            op_flag = True
            opers.append(c)

        elif c in nums:
            if op_flag:
                numbers.append(c)
            else:
                numbers.append(numbers.pop(-1) + c)
            op_flag = False
        else:
            print('oper error')
            return -1

    value = int(numbers[0])
    for n, o in zip(numbers[1:], opers):
        n = int(n)

        if o == operations[0]:
            value += n
        elif o == operations[1]:
            value -= n
        elif o == operations[2]:
            value *= n
        elif o == operations[3]:
            value = value // n
        else:
            print('oper error')
            value = -1
            return -1
    return value


def make_expr(N, target) -> int:
    q = deque(N)
    visit = deque()
    MAX_COUNT = 8
    count = 0

    while q:

        curr = q.popleft()

        # if get_value(curr) == target:
        if eval(curr) == target:
            print(curr)
            return curr.count(N)

        if curr not in visit:
            if curr.count(N) > MAX_COUNT:
                break
            visit.append(curr)
            q.append(curr + "+" + N)
            q.append(curr + "-" + N)
            q.append(curr + "*" + N)
            q.append(curr + "/" + N)
            q.append(curr + N)

    return -1


def solution(N, number):
    N = str(N)
    return make_expr(N, number)


# case 1
N, number = 5, 12

# case 2
# N, number = 5, 31168


# N, number = 5, 24


print(solution(N, number))
