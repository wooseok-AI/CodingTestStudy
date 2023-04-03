n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

def dp_solution(N, schedule):
    dp = [0] * (n + 1)

    for i in range(n-1, -1, -1):
        t, p = schedule[i]
        if i + t <= n:
            dp[i] = max(p + dp[i + t], dp[i + 1])
        else:
            dp[i] = dp[i + 1]

    print(dp[0])


def dfs_solution(day, profit):
    global maximum_profit

    if day == n:
        maximum_profit = max(maximum_profit, profit)
        return

    if day + schedule[day][0] <= n:
        dfs_solution(day+schedule[day][0], profit + schedule[day][1])

    dfs_solution(day+1, profit)


maximum_profit = 0

for day in range(n):
    dfs_solution(day, 0)

print(maximum_profit)





