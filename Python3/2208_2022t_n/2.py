import math
def solution(levels):
    levels.sort()
    if len(levels) < 4:
        return levels[-1]

    limit = len(levels)*(1 - 0.25)
    # limit = round(limit)
    print(limit)
    limit = math.ceil(limit)
    print(limit)
    print(1-(limit/len(levels)))

    # print(levels[limit:])
    # print(min(levels[limit:]))
    # return min(levels[limit:])
    return levels[limit]
#
# solution([1,2,3,4])

# solution(list(range(234)))
print(solution(list(range(1,10))))

print(solution([1,2]))
