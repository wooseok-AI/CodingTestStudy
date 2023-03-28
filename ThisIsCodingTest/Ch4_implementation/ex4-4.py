def solution(N, M, A, B, d, Map):
    visited = list()
    visited.append([A, B])
    current = [A, B]

    # 방향 인덱스 [북, 동, 남, 서]
    # 뒤로 가는 방향에 바다가 있으면 정지
    # 방위별 인텍스 (row or col, 더하는 수)
    # 왼쪽으로 회전 후, 전진
    forward_direction = [[0, -1], [1, 1], [0, 1], [1, -1]]
    ocean = False
    while not ocean:
        # 루프 탈출 후, 뒷 방향이 바다면 ocean = True
        # 네번의 시도 중에 다음 방향이 결정되면 루프 재시작
        for trial in range(4):
            # 다음 방향의 위치 좌표: 왼쪽 회전 후 한칸 전진
            # 방향 기준 왼쪽 회전, 3 더한 후 4로 나눈 나머지
            # 뒷방향: 1 더하고 4로 나눈 나머지
            next_direction = (d + 3) % 4
            next_pos_info = forward_direction[next_direction]
            # 다음 위치 좌표
            next_pos = current.copy()
            next_pos[next_pos_info[0]] += next_pos_info[1]
            print(next_pos)
            # 다음 위치 좌표를
            if next_pos not in visited and Map[next_pos[0]][next_pos[1]] == 0:
                    current = next_pos.copy()
                    visited.append(current)
                    d = next_direction
                    continue
            else:
                if trial < 3:
                    d = next_direction
                    continue
                else:
                    next_direction = (d + 1) % 4
                    back_pos_info = forward_direction[next_direction]
                    back_pos = current.copy()
                    back_pos[back_pos_info[0]] += back_pos_info[1]
                    if Map[back_pos[0]][back_pos[1]] == 1:
                        ocean = True
                        continue

    return len(visited)


if __name__ == "__main__":
    N, M = map(int, input("맵 생성 : ").split())  # N * B 맵 생성
    A, B, d = map(int, input("(A, B) 에 d 방향을 보고 있는 캐릭터 : ").split())
    Map = []
    for m in range(N):
        row_map = list(map(int, input("육지 0 바다 1 : ").split()))
        Map.append(row_map)
    print(solution(N, M, A, B, d, Map))
