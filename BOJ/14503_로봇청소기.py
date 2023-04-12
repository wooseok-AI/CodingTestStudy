
def rotate(d):
    return (d + 3) % 4

def check_room(n, m, grid, x, y, d):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        d = rotate(d)
        nx = x + dx[d]
        ny = y + dy[d]
        # 청소할 곳이 있다면 전진
        if grid[nx][ny] == 0:
            return d
    # 한바퀴 회전 이후에도 청소되지 않는 빈칸이 없다면 후진 준비
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 청소 횟수
    cnt = 0

    while True:
        # 현재 칸을 청소해야할때.
        if grid[r][c] == 0:
            cnt += 1
            grid[r][c] = 2

        # 청소할 다음 칸 찾기
        next_d = check_room(N, M, grid, r, c, d)
        # 청소할 곳이 없는 경우
        if next_d == -1:
            # 반대방향
            op_d = (d + 2) % 4
            # 후진 (방향은 유지됨)
            nr = r + dx[op_d]
            nc = c + dy[op_d]
            # 뒤가 벽이면 정지
            if grid[nr][nc] == 1:
                break
            # 뒤로 한칸 이동
            else:
                r = nr
                c = nc
        else:
            r = r + dx[next_d]
            c = c + dy[next_d]
            d = next_d
    print(cnt)