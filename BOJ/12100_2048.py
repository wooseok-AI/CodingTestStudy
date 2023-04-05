N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def find_all(K):
    log = []
    dir = [0, 1, 2, 3] # 상 하 좌 우

    def combination(t_target : int, result: list):
        if len(result) == t_target:
            log.append(result)
            return

        for num in dir:
            combination(t_target, result + [num])

    for i in range(1,K+1):
        combination(i, [])

    return log


def prepare(d, board):
    line = []
    # 상 하 움직임
    if d == 0 or d == 1:
        for j in range(N):
            temp = []
            for i in range(N):
                if board[i][j] !=0:
                    temp.append(board[i][j])
            line.append(temp)

    # 좌 우 움직임
    else:
        for i in range(N):
            temp = []
            for j in range(N):
                if board[i][j] != 0:
                    temp.append(board[i][j])
            line.append(temp)

    return line


def move(d, line):
    result = []
    for l in line:
        new_line = []
        add = False
        if d == 0 or d == 2:
            for n in range(0, len(l)):
                if add:
                    add = False
                    continue
                else:
                    if not n == len(l)-1:
                        if l[n] == l[n+1]:
                            new_line.append(l[n] + l[n+1])
                            add = True
                        else:
                            new_line.append(l[n])
                    else:
                        new_line.append(l[n])
            result.append(new_line)
        if d == 1 or d == 3:
            for n in range(len(l)-1, -1, -1):
                if add:
                    add = False
                    continue
                else:
                    if not n == 0:
                        if l[n] == l[n-1]:
                            new_line.append(l[n] + l[n-1])
                            add = True
                        else:
                            new_line.append(l[n])
                    else:
                        new_line.append(l[n])
            result.append(new_line)
    return result
def new_board(d, result:list, N):
    new_board = [[0] * N for _ in range(N)]
    direction = [1, -1, 1, -1]
    start = [0,-1,0,-1]
    # 상 하
    if d == 0 or d == 1:
        for idx, line in enumerate(result):
            row = start[d]
            for i in range(len(line)):
                new_board[row][idx] = line[i]
                row += direction[d]
    if d == 2 or d == 3:
        for idx, line in enumerate(result):
            col = start[d]
            for i in range(len(line)):
                new_board[idx][col] = line[i]
                col += direction[d]
    return new_board


def one_iter(d, board):
    line = prepare(d, board)
    # print(line)
    new_line = move(d, line)
    # print(new_line)
    board = new_board(d, new_line, N)
    return board

try_set = find_all(5)
max_num = -1

for t in try_set:
    b = board
    for iter in t:
        b = one_iter(iter, b)
    for i in range(N):
        for j in range(N):
            max_num = max(max_num, b[i][j])
print(max_num)

