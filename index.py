coins = [1, 5, 10, 25]

def min_coins_recursive(change=100):
    if change == 0:
        return 0
    res = change

    for c in coins:
        if c <= change:
            r = min_coins_recursive(change-c)
            if r != change and r + 1 < res:
                res = r + 1

    return res


def min_coins_dynamic(change=100):
    coin_list = [[change] * (change + 1)] * len(coins)
    coin_list[0] = [*range(0, change + 1)]

    for i in range(0, len(coins)):
        coin_list[i][0] = 0

    for i in range(1, len(coins)):
        for j in range(1, change + 1):
            coin_list[i][j] = min(coin_list[i-1][j], 1 + coin_list[i][j - coins[i]]) if coins[i] <= j else coin_list[i-1][j]
            
    return coin_list[-1][-1]


change = 30
print("Recursive:", min_coins_recursive(change))
print("Dynamic:", min_coins_dynamic(change))
