"""
https://programmers.co.kr/learn/courses/30/lessons/42577
[Programmers] 42577 - 전화번호 목록
그래서 이문제가 왜 hash 카테고리에 있는가?
"""


# str.startswith()이용
def solution(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book[:-1],phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


# 정규표현식 이용
# import re
# def solution(phoneBook):
#
#     for b in phoneBook:
#         p = re.compile("^"+b)
#         for b2 in phoneBook:
#             if b != b2 and p.match(b2):
#                 return False
#     return True
