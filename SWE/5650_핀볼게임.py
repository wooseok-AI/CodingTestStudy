def solution(pinball_map: list, sr: int, sc: int, d: int):
    # 블럭 정의
    # 공의 방향 [북 동 남 서]
    # 북 0 동 1 남 2 서 3
    # 1번 블럭  [남쪽으로 전환, 서쪽으로 전환, 동쪽으로 전환, 북쪽으로 전환]
    # 2번 블럭  [동쪽으로 전환, 서쪽으로 전환, 북쪽으로 전환, 남쪽으로 전환]
    # 3번 블럭  [서쪽으로 전환, 남쪽으로 전환, 북쪽으로 전환, 동쪽으로 전환]
    # 4번 블럭  [남쪽으로 전환, 북쪽으로 전환, 서쪽으로 전환, 동쪽으로 전환]
    # 5번 블럭  [남쪽으로 이동, 서쪽으로 이동, 북쪽으로 이동, 동쪽으로 이동]

    d_col = [0, 1, 0, -1]
    d_row = [-1, 0, 1, 0]
    block = {1: [2, 3, 1, 0],
             2: [1, 3, 0, 2],
             3: [3, 2, 0, 1],
             4: [2, 0, 3, 1],
             5: [2, 3, 0, 1]
             }
    # 블랙홀 위치, 웜홀 위치 저장
    global hole
    map_size = len(pinball_map)
    pinball_score = 0
    move = 0
    row, col = sr, sc

    while True:
        row += d_row[d]
        col += d_col[d]
        info = pinball_map[row][col]

        if info == -1 or [row, col] == [sr, sc]:
            break
        elif info >= 6:
            row, col = hole[(row, col)]
        elif 1 <= info <= 5:
            d = block[info][d]
            pinball_score += 1

    return pinball_score


T = int(input())
for tc in range(T):
    N = int(input())
    pinball_map = []
    hole_index = [0] * 11
    hole = dict()
    pinball_map.append([5] * (N+2))
    for r in range(N):
        R = list(map(int, input().split()))
        pinball_map.append([5] + R + [5])
        for c in range(N):
            num = R[c]
            if 6 <= num <= 10:
                if not hole_index[num]:
                    hole_index[num] = (r+1, c+1)
                else:
                    hole[(r+1, c+1)] = hole_index[num]
                    hole[hole_index[num]] = (r+1, c+1)
    pinball_map.append([5] * (N+2))

    best_score = -1
    for sr in range(1, N+1):
        for sc in range(1, N+1):
            if pinball_map[sr][sc] == 0:
                for d in range(4):
                    score = solution(pinball_map, sr, sc, d)
                    best_score = max(best_score, score)
    print("#{} {}".format(tc+1, best_score))

    # print(solution(pinball_map, 6, 3, 3))
