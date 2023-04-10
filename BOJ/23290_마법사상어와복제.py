from collections import defaultdict, deque
from copy import deepcopy
M, S = map(int, input().split())
base = [[0] * 4 for _ in range(4)]
smell = defaultdict(list)
smell_map = [[0] * 4 for _ in range(4)]
# 첫 시도에는 냄새 x
smell[0] = deepcopy(smell_map)


for _ in range(M):
    x, y, d = map(int, input().split())
    if not base[x-1][y-1]:
        base[x-1][y-1] = [d-1]
    else:
        base[x-1][y-1].append(d-1)
i, j = map(int, input().split())
shark = (i-1,j-1)

def task1(array):
    return deepcopy(array)

def task2(array, smell, trial, shark):
    temp_base = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # 물고기가 있는 경우, 0이 아님
            if not base[i][j]:
                continue
            fish_list = deepcopy(base[i][j])
            base[i][j] = 0 #새로 채울 예정
            for fish in fish_list:
                nx, ny, nd = fish_move(i, j, fish, smell, trial, shark)
                if not temp_base[nx][ny]:
                    temp_base[nx][ny] = [nd]
                else:
                    temp_base[nx][ny].append(nd)
    return temp_base

def fish_move(x, y, d, smell, trial, shark):
    dx, dy = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
    for i in range(8):
        nd = (d + 7*i) % 8
        nx, ny = x + dx[nd], y + dy[nd]
        if 0<= nx<4 and 0<=ny<4 and (nx, ny) != shark:
            if trial > 2:
                # 3번째 시도부터는 전전 냄새와 전 냄새 보두 참조, 상어 여부
                if not smell[trial-1][nx][ny] and not smell[trial-2][nx][ny]:
                    return nx, ny, nd
            else:# 두번째 시도까지는 이전 냄새만 보면 됨
                if smell[trial-1][nx][ny] == 0:
                    return nx, ny, nd
        else: #범위 벗어나면 다른 방향
            continue
    return x, y, d

def task3(base:list, smell, trial, shark):
    dx, dy = (0, -1, 0, 1, 0), (0, 0, -1, 0, 1)
    possible_move = every_move(shark)
    x, y = shark
    max_eat = -1
    eat_record = defaultdict(list)
    for move in possible_move:
        nx, ny = x, y
        eat = 0
        temp_base = deepcopy(base)
        for m in move:
            nx, ny = nx + dx[m], ny + dy[m]
            if not temp_base[nx][ny]:
                continue
            eat += len(temp_base[nx][ny])
            temp_base[nx][ny] = 0
        max_eat = max(max_eat, eat)
        eat_record[eat].append(int("".join(map(str, move))))
        # eat_record[eat].sort()
    next_move = eat_record[max_eat][0]

    for i in str(next_move):
        nx, ny = x + dx[int(i)], y + dy[int(i)]
        if base[nx][ny]:
            base[nx][ny] = 0
            smell[trial][nx][ny] = 1
        x, y = nx, ny
    shark = (x, y)

    return base, smell, shark

def every_move(shark):
    temp = [1, 2, 3, 4]
    log = []
    # visited = [[0] * 4 for _ in range(4)]
    dx, dy = (0, -1, 0, 1, 0), (0, 0, -1, 0, 1)

    def dfs(x, y, array):
        if len(array) == 3:
            log.append(array)
            return

        for i in temp:
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4: #and not visited[nx][ny]:
                # visited[nx][ny] = 1
                dfs(nx, ny, array + [i])
                # visited[nx][ny] = 0

    dfs(shark[0],shark[1],[])
    return log

def task5(base:list, dup:list):

    for i in range(4):
        for j in range(4):
            if dup[i][j]:
                new = deepcopy(dup[i][j])
                if not base[i][j]:
                    base[i][j] = new
                else:
                    base[i][j] += new
    return base



for trial in range(1,S+1):
    smell[trial] = deepcopy(smell_map)
    # 1번 복제
    duplicate = task1(base)
    # 2번 물고기 이동
    base = task2(base, smell, trial, shark)
    # if trial == 3:
    #     print("fish move\n",base)
    # 상어이동
    base, smell, shark = task3(base, smell, trial, shark)
    # 냄새 없어짐
    if trial >=3:
        smell[trial-2] = [[0] * 4 for _ in range(4)]
    # 복제
    base = task5(base, duplicate)
    # print(base)
    # print(shark)
    # print(smell[trial])
    # print('\n')

total_len = 0
for i in range(4):
    for j in range(4):
        if base[i][j]:
            total_len += len(base[i][j])

print(total_len)