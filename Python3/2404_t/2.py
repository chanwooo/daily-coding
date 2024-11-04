def solution(s):
    max_num = -1
    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            max_num = max(max_num, int(s[i]+s[i+1]+s[i+2]))

    return max_num

a = "111999333"
result = solution(a)
print(result)

