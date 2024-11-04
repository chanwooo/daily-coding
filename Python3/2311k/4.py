from itertools import combinations

global limit
global max_round


def solution(coin, cards):
    n = len(cards)
    hand = []

    global limit, max_round
    limit = n + 1
    max_round = 0

    for i in range(n // 3):
        hand += [cards.pop(0)]

    round(cards, 1, hand, coin)

    return max_round


def round(cards, game_round, hand, coin):
    # print(game_round, hand, cards, coin)

    global max_round
    max_round = game_round if game_round > max_round else max_round

    if coin < 2:
        return 0

    if len(cards) < 2:
        return 0

    if game_round > 50:
        return -1

    try:
        # 턴시작 2장 드로우
        card1 = cards.pop(0)
        card2 = cards.pop(0)

        # 안먹을 때
        check_pair(hand, cards, game_round, coin)

        # 1장 먹을때(0)
        coin -= 1
        hand.pop(0)
        check_pair(hand, cards, game_round, coin)
        hand.insert(0, card1)

        # 1장 먹을때(1)
        hand.pop(1)
        check_pair(hand, cards, game_round, coin)
        hand.insert(1, card2)

        # 2장 먹을때
        coin -= 1
        if coin < 0:
            return 0
        hand += [card1]
        hand += [card2]
        check_pair(hand, cards, game_round, coin)


    except IndexError:
        return 0


def check_pair(hand, cards, game_round, coin):
    global limit
    pair = list(combinations(hand, 2))
    flag = False
    for p in pair:
        if sum(p) == limit:
            flag = True
            # print(p, hand, coin)
            try:
                hand.remove(p[0])
                hand.remove(p[1])
                round(cards, game_round + 1, hand, coin)

            except ValueError:
                return 0

    if not flag:
        # round(cards, game_round, hand, coin)
        return 0


print("5->", solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))  # 5
print("2->", solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))  # 2
print("4->", solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))  # 4
print("1->", solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))  # 1
