
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    max_val = float('inf')
    dp = [0] + [max_val] * amount
    coin_count = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_count[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result