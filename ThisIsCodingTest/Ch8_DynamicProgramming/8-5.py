X = int(input())

def solution(X):
    dp = [0] * 30
    for i in range(2, X+1):
        dp[i] = dp[i-1] + 1

        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i//5] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
    print(dp)
    return dp[X]

print(solution(X))