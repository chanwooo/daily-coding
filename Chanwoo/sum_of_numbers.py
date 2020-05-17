"""
https://www.acmicpc.net/problem/2003
[Boj] 2003 - 수들의 합 2
"""

#
# N, M = map(int, "4 2".split(' '))
# A = list(map(int, "1 1 1 1".split(' ')))
#
# N, M = map(int, "10 5".split(' '))
# A = list(map(int, "1 2 3 4 2 5 3 1 1 2".split(' ')))

N, M = map(int, input().split(' '))
A = list(map(int, input().split()))

start = 0
end = 0
cur = 0
count = 0

while True:
    # print(start, end, count, A[start:end+1], sum(A[start:end+1]))
    if start > N or end >= N:
        break

    cur = sum(A[start:end + 1])

    if cur > M:
        start += 1
    elif cur < M:
        end += 1
    else:
        count += 1
        end += 1

print(count)
