def solution(s):
    check = set()
    answer = []
    for i in range(1, len(s) - 1):
        # print(s[i-1:i+2])
        for c in s[i - 1:i + 2]:
            check.add(c)

        if len(check) == 1:
            # print("find")
            answer.append(int(s[i - 1:i + 2]))
        check = set()

    # print(answer)
    if answer:
        return max(answer)
    else:
        return -1
    # return max(answer) if not answer else -1