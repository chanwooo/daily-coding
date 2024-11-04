# ...x..xxx.xxx
# 연속된 포트홀을 고치는데 포트홀개수+1 비용이 필요
# 비용으로 고칠수있는 포트홀의 수


def sol(S, B):
    S += "."
    pot = []

    count = 0
    for s in S:
        if s == "x":
            count += 1
        else:
            if count == 0:
                continue
            pot.append(count)
            count = 0

    pot.sort(reverse=True)

    answer = 0
    cost = 0
    for p in pot:
        answer += p
        cost = cost + p + 1
        if cost > B:
            answer = answer + B - cost
            break

    return answer


print(sol("..x..x..xxx.xxx", 7)) # 5
print(sol("..x..x..xxx.xxx", 10)) # 7
print(sol("..x..x..xxx.xxx", 20)) # 5
print(sol(".xxxxxx7.x2.xx3.x2..x2..x2.xxx4.x2", 20)) # 13

