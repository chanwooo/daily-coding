import re


def solution(amountText):
    # 1, 정규식으로 숫자 또는 ,가 있는지 검사
    patt = r"[^0-9,]"
    result = re.findall(patt, amountText)
    if result:
        return False

    # 0으로 시작
    if amountText[0] == "0":
        if len(amountText) == 1:
            return True
        return False

    # 콤마 자리 틀림
    if "," in amountText:
        reverse = amountText[::-1]
        for i in range(len(amountText)):
            if i % 4 == 3:
                if reverse[i] != ",":
                    return False
            else:
                if not reverse[i].isdigit():
                    return False

    print(result)

    return amountText


a = "0"
result = solution(a)
print(result)
