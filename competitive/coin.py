def coin_change(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for i in range(1,amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i],dp[i-coin]+1)

    return dp[amount]


if __name__ == "__main__":
    print(coin_change([1,2,5],11))
