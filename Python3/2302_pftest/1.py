def isPower(arr):
    # Write your code here
    answer = []
    for a in arr:
        if a == 0:
            answer.append(0)
        elif (a & (a - 1)) == 0:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(isPower([3, 2, 3, 4, 1024]))

# 2의 거듭제곱수면 1, 아니면 0을 리스트에 반환
