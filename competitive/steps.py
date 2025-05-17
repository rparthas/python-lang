def steps(top):
    dp = [0]*(top+1)
    dp[1] = 1
    dp[2] = 2
    # dp[2] = 2
    for i in range(3,top+1):
      dp[i] = dp[i-1] + dp[i-2]

    return dp[top]

if __name__ == "__main__":
    print(steps(5))
