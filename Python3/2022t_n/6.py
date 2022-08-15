from collections import defaultdict
def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    print("sol1")
    data = defaultdict(int)
    for i in range(len(steps_one)):
        data[names_one[i]] += steps_one[i]
    for i in range(len(steps_two)):
        data[names_two[i]] += steps_two[i]
    for i in range(len(steps_three)):
        data[names_three[i]] += steps_three[i]

    data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    data = list(map(lambda x: x[0], data))

    print(data)


def solution2(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    print("sol2")
    walk_dict = defaultdict(int)
    for i in range(len(steps_one)):
        walk_dict[names_one[i]] += steps_one[i]
    for i in range(len(steps_two)):
        walk_dict[names_two[i]] += steps_two[i]
    for i in range(len(steps_three)):
        walk_dict[names_three[i]] += steps_three[i]

    step_dict = defaultdict(list)
    for name, step in walk_dict.items():
        step_dict[step].append(name)
    walk_list = sorted(step_dict.items(), key=lambda x: x[0], reverse=True)

    answer = []
    for names in walk_list:
        answer += sorted(names[1])

    print(answer)



solution(
    [1, 2, 3], ["james", "bob", "alice"],
    [10, 20, 30], ["james", "alice", "bob"],
    [1000, 1, 1], ["bob", "alice", "james"]
)
# ['bob', 'alice', 'james']


solution(
    [0, 5, 1], ["evan", "ed", "evan"],
    [9999], ["rose"],
    [1], ["richard"]
)
# ['rose', 'ed', 'evan', 'richard']

solution(
    [100, 100, 100], ["ccc", "aaa", "bbb"],
    [100, 100, 100], ["ccc", "aaa", "bbb"],
    [100, 100, 100], ["ccc", "aaa", "bbb"]
)
# ['aaa', 'bbb', 'ccc']

solution2(
    [1, 2, 3], ["james", "bob", "alice"],
    [10, 20, 30], ["james", "alice", "bob"],
    [1000, 1, 1], ["bob", "alice", "james"]
)

solution2(
    [0, 5, 1], ["evan", "ed", "evan"],
    [9999], ["rose"],
    [1], ["richard"]
)

solution2(
    [100, 100, 100], ["ccc", "aaa", "bbb"],
    [100, 100, 100], ["ccc", "aaa", "bbb"],
    [100, 100, 100], ["ccc", "aaa", "bbb"]
)
