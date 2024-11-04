def solution(levels):
    levels.sort()
    # print(len(levels)//4)
    # print(levels[-(len(levels)//4)])
    if len(levels)<4:
        return -1
    return levels[-(len(levels)//4)]



a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = solution(a)
print(result)

