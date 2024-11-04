import sys

si = sys.stdin.readline
n, K = map(int, si().split())

comb = [list(map(int, si().split())) for _ in range(n)]

A = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        A[i][j] = comb[j].count(i)

dp = [[0 for _ in range(n)] for _ in range(K + 1)]

for i in range(n):
    dp[1][i] = 1

MOD = 100000007
for cnt in range(2, K + 1):
    for i in range(n):
        for j in range(n):
            dp[cnt][i] += A[i][j] * dp[cnt - 1][j]
            dp[cnt][i] %= MOD

print(*dp[K])

'''
2 3
0 1
1 0
=>
4 4

2 4
0 0
0 0
=>
16 0

'''
