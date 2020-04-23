"""
[Programmers] 60057 - 문자열 압축

https://programmers.co.kr/learn/courses/30/lessons/60057
2020 카카오 공채 코딩테스트 기출
"""
def solution(s):
    L = len(s)
    result = []


    if L == 1:
        return 1

    for unit in range(1, L//2+1):
        comp_str = ""

        count = 1

        print()
        print("unit :",unit)

        for i in range(unit, L + unit, unit):
            # print(i,i+unit,i-unit,i, s[i:i+unit], s[i-unit:i])

            print(">", i, s[i:i+unit], s[i-unit:i], count)
            if s[i:i+unit] == s[i-unit:i]:
                count += 1
            else:
                if count > 1:
                    print(s[i-unit:i], count)
                    comp_str += str(count)+s[i-unit:i]
                    count = 1
                else:
                    print(s[i-unit:i])
                    comp_str += s[i - unit:i]
                # print(s[i:i+unit])
                # print('comp',count)
        print(i,"?")
        print(comp_str)
        result.append(len(comp_str))
    print(result)
    return min(result)



# s = "aaaba"  # 2
# s = "aabbaccc"  # 7
s = "ababcdcdababcdcd"  # 9
# s = "abcabcdede"  # 8
# s = "abcabcabcabcdededededede"  # 14
# s = "xababcdcdababcdcd"  # 17

# s = "b"

print(solution(s))