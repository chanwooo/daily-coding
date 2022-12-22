convt = {"A": 0,
         "B": 1,
         "C": 2,
         "D": 3,
         "E": 4,
         "F": 5,
         "G": 6,
         "H": 7,
         "J": 8,
         "K": 9,
         }


# 아무것도 없이 비어있으면 2
# 한자리
# 1번, 10번 자리가 차있으면 2
# 2,3,8,9 있으면 1

# 2인경우
# 000 0000 000
# 100 0000 000
# 000 0000 001
# 100 0000 001

# 1인경우
# 001 0000 000
# 011 0000 000
# 111 0000 000
# 000 0000 100
# 000 0000 110
# 000 0000 111
# 001 0000 100
# ...

# 0인경우
# 000 1001 000
# 000 1111 000
# 111 1111 111


# 1,2,3,7,8,9 =>1

def solution(N, S):
    result = 0
    seat = [["o"] * 10 for _ in range(N)]

    if S:
        for s in S.split(" "):
            print(s)

            seat[int(s[0:-1]) - 1][convt[s[-1]]] = "x"

    for st in seat:
        st = "".join(st)
        if st in ["oooooooooo", "xooooooooo", "ooooooooox", "xoooooooox"]:
            result += 2
        elif st[3:7] == "oooo":
            result += 1
        elif st[1:5] == "oooo":
            result += 1
        elif st[5:9] == "oooo":
            result += 1

    print(seat)

    return result


# print(solution(2,"1A 2F 1C"))
# print(solution(22, '1A 3C 2B 20G 5A'))
print(solution(1, ''))
