# Fibonacci Funtion using DP

dp = [0] * 100

def fibo_recursion(x):

    if x == 1 or x == 2:
        return 1

    if dp[x] != 0:
        return dp[x]

    dp[x] = fibo_recursion(x-1) + fibo_recursion(x-2)
    return dp[x]


def fibo_iteration(x):

    if x == 1 or x == 2:
        dp[x] = 1
    else:
        for idx in range(3, x+1):
            dp[idx] = dp[idx-1] + dp[idx-2]

    return dp[x]

dp[1] = 1
dp[2] = 1
print(dp)
print(fibo_iteration(99))

print(dp)