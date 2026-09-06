coins = [1, 2, 5, 10, 20, 50, 100, 200]

def count(amount: int, coins_list: list[int]):
    ways = [0] * (amount+1)
    ways[0] = 1

    for i in range(len(coins_list)):
        for j in range(coins[i], amount+1):
            # here, j is the 'remaining' pence left
            ways[j] = ways[j] + ways[j-coins[i]]
    return ways


print(count(200, coins)[200])
