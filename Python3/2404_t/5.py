import math


def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료

    # vat = 과세금액의 10%
    # vat = 주문금액 - 공급가액
    # 주문금액 = 공급가액 + 부가가치세 => 공급대가 if 봉사료 가있으면 뺴야됨

    # 과세금액 = 공급가액 - 비과세금액

    if orderAmount - taxFreeAmount == 1:
        return 0
    amount = orderAmount - taxFreeAmount - serviceFee


    return calcVAT(amount)


# 부가가치세 = 과세금액 의 10%, 소수첫자리 올림
def calcVAT(amount):
    amount = amount / 10
    return math.ceil(amount)


print(solution(100, 0, 0))
print(solution(120, 20, 0))
print(solution(120, 0, 20))
print(solution(1, 0, 0))
print(solution(11, 0, 0))
