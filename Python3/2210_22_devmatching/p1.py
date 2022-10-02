import re


def solution_(registered_list, new_id):
    if new_id not in registered_list:
        return new_id
    else:
        s = re.sub(r'[0-9]', '', new_id)
        n = re.sub(r'[^0-9]', '', new_id)

        if not n:
            n = 0
        n = int(n)

        r = []
        max_rn = 0
        for rl in registered_list:
            if s in rl:
                rn = re.sub(r'[^0-9]', '', rl)
                if not rn:
                    rn = 0
                rn = int(rn)

                if max_rn < int(rn):
                    max_rn = int(rn)
                r.append(int(rn))
        r.sort()
        print(r)
        print(list(range(n, max_rn+1)))
        setr = set(r)
        setmaxrn = set(range(n,max_rn+1))
        setr.symmetric_difference_update(setmaxrn)
        print(setr)
        if not setr:
            setr = [max_rn+1]
        print(min(setr))


        new_id = s + str(min(setr))



        return new_id



# 제출한 코드

import re


def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id
    else:
        s = re.sub(r'[^a-z]', '', new_id)
        n = re.sub(r'[^0-9]', '', new_id)

        if not n:
            n = 1
        n = int(n)

        new_id = s + str(n)

        while new_id in registered_list:
            # print(registered_list)
            registered_list.remove(new_id)
            n += 1
            new_id = s + str(n)
            # print(new_id)

        return new_id



print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace16"))

print(solution(["bird99", "bird98", "bird101", "gotoxy", "bird100", "bird103"], "bird98"
               ))

print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98")) # bird100


print(solution(
    ["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))
# cow10
