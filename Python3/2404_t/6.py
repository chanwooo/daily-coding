def solution(money, stocks):
    answer = 0

    def buy_stock(index, buy_money, value):
        nonlocal answer

        if index == len(stocks) or buy_money + stocks[index][1] > money:
            answer = max(answer, value)
            return

        for next_index in range(index + 1, len(stocks) + 1):
            buy_stock(next_index, buy_money + stocks[index][1], value + stocks[index][0])

    for i in range(len(stocks)):
        buy_stock(i, 0, 0)

    return answer


a = [1,2,3,4]
print(a[1:0])