N, M = list(map(int, input().split()))
board = []

for r in range(N):
    row = [x for x in input()]
    board.append(row)
    if 'R' in row:
        R = [r, row.index('R')]
        row[row.index('R')] = '.'
    elif 'B' in row:
        B = [r, row.index('B')]
        row[row.index('B')] = '.'
    elif 'O' in row:
        O = [r, row.index('O')]
        row[row.index('O')] = '.'

def move(R, B, x_axis, y_axis,board, cnt):
    Fail = False
    while board[R[0]][R[1]] != '#' and board[B[0]][B[1]] != '#':
        cnt+=1
        if board[R[0]][R[1]] != '#' or A == O:
            R[0] += 0
            R[1] += 0
        else:
            R[0] += x_axis
            R[1] += y_axis
            
        if board[B[0]][B[1]] != '#' or B==O:
            B[0] += 0
            B[1] += 0
            break            
        else:
            B[0] += x_axis
            B[1] += y_axis

    return R,B,cnt, Fail

def search(board, R,B, prev, x_axis, y_axis):
    
    prev = [A, B, x_axis, y_axis]
    
    if A == O:
        Rin = True
    else:
        Rin = False
        
    if B == O:
        Bin = True
    else:
        Bin = False
    
    