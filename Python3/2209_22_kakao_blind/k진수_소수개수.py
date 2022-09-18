def solution(n, k):
    answer = 0
    nk = convert(n, k)
    nums = nk.split("0")

    for num in nums:
        if is_prime(num):
            answer += 1
    return answer


import string
tmp = string.digits + string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime(k):
    if k == '':
        return False
    k = int(k)
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


print(solution(437674, 3))
print(solution(110011, 10))
