from typing import List


def foo(games: List[str]) -> int:
    score = 0

    if len(games) != 10:
        raise Exception("10게임을 입력하세요.")

    for game in games:
        home, away = map(int, game.split(":"))
        if not 0 <= home <= 4 or not 0 <= away <= 4:
            raise ValueError("점수는 0~4점 사이")

        if home > away:
            score += 3
        elif home == away:
            score += 1

    return score


print(foo(["1:0", "2:0", "1:0", "3:0", "4:1", "3:0", "2:0", "2:0", "2:0", "2:0"]))
print(foo(["1:1", "2:2", "1:1", "0:0", "1:3", "3:0", "2:0", "2:0", "2:0", "2:0"]))
