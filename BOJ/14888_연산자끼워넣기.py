N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split())) # "+ - * / " 0123
c = []
for idx in range(len(cal)):
    for _ in range(cal[idx]):
        c.append(idx)


# 중복 없는 순열
check = [0] * len(c)
log = set()
# print(c)

def dfs(c, num, check, array):

    if len(array) == num:
        log.add(tuple(array))

    for i in range(len(c)):
        if not check[i]:
            check[i] = 1
            dfs(c, num, check, array + [c[i]])
            check[i] = 0


# A = [1,2,3,4,5,6]
# log = [(0,0,1,2,3),(3,0,0,1,2),(0,3,2,1,0),(3,2,1,0,0)]
# N = 6
dfs(c, N-1, check, [])
MAX, MIN = -int(1e9), int(1e9)
# print(log)
for perm in log:
    result = 0
    for x in range(N):
        if x == 0:
            result = A[x]
        else:
            op = perm[x-1]
            if op == 0:
                result = result + A[x]
            elif op == 1:
                result = result - A[x]
            elif op == 2:
                result = result * A[x]
            elif op == 3:
                if result <0:
                    result = -(abs(result)//A[x])
                else:
                    result = result//A[x]
    if result > MAX:
        MAX = result
    if result < MIN:
        MIN = result

print(MAX)
print(MIN)


