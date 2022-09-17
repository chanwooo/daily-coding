def solution(id_list, report, k):
    report_dict = {id: list() for id in id_list}
    report = list(set(report))

    mail_dict = {id: 0 for id in id_list}

    for r in report:
        a, b = r.split(" ")
        report_dict[b].append(a)
    # print(report_dict)

    for key in report_dict:
        if len(report_dict[key]) >= k:
            # print(report_dict[key], key)
            for user in report_dict[key]:
                mail_dict[user] += 1
    # print(mail_dict.values())
    return list(mail_dict.values())


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
               2))  # [2, 1, 1, 0]

print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))  # [0,0]
