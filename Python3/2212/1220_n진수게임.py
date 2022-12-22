import string


def solution(n, t, m, p):
    full_answer = ""
    my_answer = ""

    l = t * m
    for i in range(l):
        full_answer += convert(i, n)

    print(full_answer)
    for idx, digit in enumerate(full_answer):
        if (idx + p) % m-1 == 0:
            my_answer += digit
            print(digit)

    print(my_answer)
    return my_answer[:t]


tmp = string.digits + string.ascii_uppercase


# 1 2 3 4
# 1 3
# 2 4


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


print(solution(2, 4, 2, 1))  # "0111"
print(solution(16, 16, 2, 1))  # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
# print(solution(16, 16, 3, 2))
# 258BE01316191C1F
