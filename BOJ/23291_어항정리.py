import copy
def add_fish(bowl: list):
    min_fish = min(bowl)
    for idx, fish in enumerate(bowl):
        if fish == min_fish:
            bowl[idx] += 1
    return bowl


# 한번 회전해서 쌓기위한 준비
def find_bowl(grid):
    # 탐색 해야하는 층수 계산
    # 남은 부분의 길이가 길면 temp_grid 반환
    temp_grid = grid.copy()
    start_col = 0
    N = len(grid)
    if grid[-1][0] is not None:
        grid[-2][1], grid[-1][0] = grid[-1][0], None
        return grid, None, None, None

    for j in range(N):
        if grid[-1][j] is not None:
            start_col = j
            break
    array = []
    # 회전시킬 어레이 찾기
    # print(grid[-4:])
    for x in range(N-1):
        flag = 0
        temp = []
        for y in range(start_col, N-1):
            if grid[x][y] is not None:
                temp.append(grid[x][y])
                flag = 1
                grid[x][y] = None
            else:
                if flag:
                    array.append(temp)
                    break

    rest_len = len([x for x in grid[-1] if x is not None])
    # print(array)
    if array == [] or rest_len - len(array[0]) < len(array) + 1:
        return temp_grid, array, start_col, None
    else:
        col_len = len(array[0])
        last_line = []
        for last in range(start_col, start_col + col_len):
            last_line.append(grid[-1][last])
            grid[-1][last] = None
        array.append(last_line)
        return grid, array, start_col, rest_len

    # # 회전할 어레이의 길이가 남은 부분보다 길면 안됨.
    # rest_len = len([x for x in grid[-1] if x is not None])
    # if rest_len < len(array):
    #     rest_len = None
    #     return temp_grid, array, start_col, rest_len
    # else:
    #     return grid, array, start_col, rest_len


def rotate_array(array: list):
    n_row = len(array)
    n_col = len(array[0])
    new_array = [[0] * n_row for _ in range(n_col)]

    for j in range(n_col):
        for i in range(n_row):
            new_array[j][n_row-1-i] = array[i][j]

    return new_array


def add_bowl(grid, array, start_col):
    new_bowl = rotate_array(array)
    start_row = (len(grid)-1) - len(new_bowl)
    for new_row in range(len(new_bowl)):
        for new_col in range(len(new_bowl[0])):
            grid[start_row+new_row][start_col+len(array[0])+new_col] = new_bowl[new_row][new_col]
    # print(grid)
    bowl = []
    for x in range(start_row, len(grid)):
        row = []
        for y in range(start_col+len(array[0]), len(grid)):
            row.append(grid[x][y])
        bowl.append(row)
    # print(bowl)
    return grid, bowl


def arrange_fish(bowl):
    # 한번씩만 연산하므로, 오른쪽과 아래만 보면됨
    dx, dy = (0, 1), (1, 0)
    temp = [[0] * len(bowl[0]) for _ in range(len(bowl))]

    for x in range(len(bowl)):
        for y in range(len(bowl[0])):
            if bowl[x][y] is None:
                continue
            else:
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(bowl) and 0<= ny <len(bowl[0]):
                        if bowl[nx][ny] is not None:
                            d = abs(bowl[x][y] - bowl[nx][ny]) // 5
                            if d > 0:
                                if bowl[x][y] > bowl[nx][ny]:
                                    temp[x][y] -= d
                                    temp[nx][ny] += d
                                else:
                                    temp[x][y] += d
                                    temp[nx][ny] -= d
    # print("temp :",temp)
    for i in range(len(bowl)):
        for j in range(len(bowl[0])):
            if bowl[i][j] is not None:
                bowl[i][j] += temp[i][j]

    return bowl

def flatten(bowl):
    flat_bowl = []
    for j in range(len(bowl[0])):
        for i in range(len(bowl)-1, -1, -1):
            if bowl[i][j] is not None:
                flat_bowl.append(bowl[i][j])
    return flat_bowl

def rotate_twice(bowl):
    result = []
    # 1번 회전
    bowl1, bowl2 = bowl[:len(bowl)//2], bowl[len(bowl)//2:]
    result.append(bowl1[::-1])
    result.append(bowl2)
    # 2번 회전
    top = []
    bottom = []
    for i in range(2):
        top.append(result[i][:len(result[0])//2])
        bottom.append(result[i][len(result[0])//2:])

    top_rotate = rotate_array(rotate_array(top))

    return top_rotate + bottom


if __name__ == "__main__":
    N, K = map(int, input().split())
    bowl = list(map(int, input().split()))
    # 가상의 공간
    T = 0
    diff = 999
    while True:
        # if T == 2:
        #     print(bowl)
        #     break
        if diff <= K:
            print(T)
            break
        T += 1
        grid = [[None] * N for _ in range(N - 1)]
        bowl = add_fish(bowl)
        grid.append(bowl)

        trial = 1
        while True:
            temp_grid = copy.deepcopy(grid)
            if trial == 1:
                grid, _, _, _ = find_bowl(grid)
            else:
                grid, array, start_col, rest_len = find_bowl(grid)
                if rest_len is None:
                    grid = temp_grid
                    break
                else:
                    grid, bowl = add_bowl(grid, array, start_col)
            trial += 1
        # print(bowl)
        arranged_bowl = arrange_fish(bowl)
        # print("arranged :", arranged_bowl)

        flat_bowl = flatten(arranged_bowl)
        # print("flatten : ", flat_bowl)

        rotate_bowl = rotate_twice(flat_bowl)
        # print("rotate : ", rotate_bowl)

        arranged_bowl2 = arrange_fish(rotate_bowl)
        # print("arranged :", arranged_bowl2)

        bowl = flatten(arranged_bowl2)
        # print("flatten : ", bowl)
        diff = max(bowl) - min(bowl)
        # print("\n")