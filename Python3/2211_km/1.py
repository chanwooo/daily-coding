def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        if enable_print >= 1:
            print(N % 10, end="")
        N = N // 10

solution(10011)
print()
solution(432)
print()
solution(32)
print()
solution(1000)
print()

