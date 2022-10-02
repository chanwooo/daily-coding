def solution(today, terms, privacies):
    today = int(today.replace(".", ""))

    answer = []
    terms_dict = {}
    for term in terms:
        key, val = term.split()
        terms_dict[key] = int(val)

    for i, privacie in enumerate(privacies):
        date, type = privacie.split(" ")
        y, m, d = date.split(".")
        y, m, d = int(y), int(m), int(d)
        m += terms_dict[type]

        d -= 1

        if d == 0:
            m -= 1
            d = 28

        while m > 12:
            y += 1
            m -= 12


        print(y, m, d, today)

        if int(f"{y:04d}{m:02d}{d:02d}") < today:
            answer.append(i + 1)
    return answer


# print(solution(
#     "2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# # [1,3]

# print(solution(
#     "2022.05.19", ["A 36", "B 36", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2035.02.20 C"]))

print(solution("2020.01.01", ["Z 3", "D 5"],
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
