N, M, x, y, K = map(int, input().split())

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

order_list = list(map(int, input().split()))

dice = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def move_dice(order):
    global dice
    # move east
    if order == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    # move west
    elif order == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    # move north
    elif order == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    #move south
    elif order == 4:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]


direction = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]


for order in order_list:

    nx, ny = x + direction[order][0], y + direction[order][1]

    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
        # print(x,y)
        move_dice(order)
        if MAP[x][y] == 0:
            MAP[x][y] = dice[3][1]
        else:
            dice[3][1] = MAP[x][y]
            MAP[x][y] = 0
        print(dice[1][1])
    else:
        continue
