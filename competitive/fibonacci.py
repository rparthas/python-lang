def fib(n):
    if n<= 1:
        return n
   
    return fib(n-1)+ fib(n-2)
    
def fib_iter(n):
    if n<= 1:
        return n
    
    dp =[0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]

if __name__ == "__main__":
    print(fib(8))
    print(fib_iter(8))
