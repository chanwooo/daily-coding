"""
[Programmers] 60058 - 괄호 변환

https://programmers.co.kr/learn/courses/30/lessons/60058
2020 카카오 공채 코딩테스트 기출
"""


def correction_brackets(p: str) -> str:
    q = 0
    ef = False

    if len(p) == 0:
        return ""

    for i, c in enumerate(p):
        if c == '(':
            q += 1
        else:  # ')'
            q -= 1

        if q == 0:
            u = p[:i + 1]
            v = p[i + 1:]

            for i, c in enumerate(u):
                if c == '(':
                    q += 1
                else:  # ')'
                    q -= 1

                if q == -1:
                    ef = True

                if q == 0 and ef:
                    a = "(" + correction_brackets(v) + ")"

                    u = list(u[1:-1])

                    for i in range(len(u)):
                        if u[i] == '(':
                            u[i] = ')'
                        else:
                            u[i] = '('
                    u = ''.join(u)

                    return a + u

            return u + correction_brackets(v)


def solution(p):
    return correction_brackets(p)


# p = "(()())()"  # "(()())()"
# p = ")("  # "()"
p = "()))((()"  # "()(())()"
# p = "))(("

print(solution(p))
