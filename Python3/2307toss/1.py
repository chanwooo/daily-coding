def solution(s, N):
    substrings = []
    Nset = set(range(1, N + 1))

    for i in range(len(s)):
        substring = s[i:i + N]
        set_substring = set(map(int, substring))
        if Nset == set_substring:
            # print(set_substring)

            substrings.append(int(substring))

    if substrings:
        return max(substrings)
    else:
        return -1


s = "1451232125"
N = 2
result = solution(s, N)
print(result)

# 예시 실행
s = "313253123"
N = 3
result = solution(s, N)
print(result)

s = "1451232125"
N = 4
result = solution(s, N)
print(result)
