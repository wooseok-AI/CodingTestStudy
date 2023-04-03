from collections import deque, defaultdict

N = int(input())
# 학생 순서
student_queue = deque()
# 학생의 좋아하는 친구 딕셔너리 학생번호 : [친구리스트]
favorite_dict = dict()
# 학생의 자리배치 여부 딕셔너리 디폴트는 False
seat_info = defaultdict(list)

for _ in range(N**2):
    info = list(map(int, input().split()))
    student_queue.append(info[0])
    favorite_dict[info[0]] = info[1:]

# 칸마다 주변 공석 수 기록
blank_array = [2] + [3 for _ in range(N - 2)] + [2]
for _ in range(N -2):
    blank_array += [3] + [4 for _ in range(N-2)] + [3]
blank_array += [2] + [3 for _ in range(N-2)] + [2]


# # 칸마다 앉아 있는 학생 번호 기록
seat_array = [0 for _ in range(N**2)]

# 방향
dr = [0,0,1,-1]
dc = [1,-1,0,0]

for student in student_queue:
    # print("student_number : ", student)
    # 해당학생의 친한 친구 목록
    fav_friend = favorite_dict[student]
    # 친구 주변 자리 저장
    temp_near_seat = [0 for _ in range(N ** 2)]
    for friend in fav_friend:
        if not seat_info[friend]:
            continue
        r, c = seat_info[friend]
        # 친구와 인접한 자리 (상하좌우)
        # 친구와 인접한 자리를 저장 하고 횟수도 저장.
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < N and 0 <= nc < N:
                nearby_index = nr*N + nc
                if seat_array[nearby_index] != 0:
                    continue
                temp_near_seat[nearby_index] += 1
                # print(student, " friend nearby: ",temp_near_seat )
    # 인접한 자리 찾기
    max_near = max(temp_near_seat)
    # 가장 인접한 자리가 다수일 떄
    if temp_near_seat.count(max_near) > 1:
        if max_near == 0:
            # print("no friend")
            seat = blank_array.index(max(blank_array))
        else:
            # 인접한 친구가 많은 자리 인덱스 r * N + c
            max_nearby_seat = [i for i, x in enumerate(temp_near_seat) if x == max_near]
            # blank array에서 공석이 제일 많은 인덱스만 추출
            # print("student can seat :", max_nearby_seat)
            max_blank = -1
            #idx는 친구와 가장 인접한 자리
            for idx in max_nearby_seat:
                if blank_array[idx] > max_blank:
                    max_blank = blank_array[idx]
                    # 순회하면 idx가 작을수록 행은 작고 열도 작음
                    seat = idx

    # 가장 인접한 자리가 하나일 떄
    else:
        seat = temp_near_seat.index(max_near)

    # print("seat :", seat)

    blank_array[seat] = -1
    # 주변 공석 업데이트
    coordinate = [seat//N, seat % N]
    seat_info[student] = coordinate
    seat_array[seat] = student
    for i in range(4):
        nr = coordinate[0] + dr[i]
        nc = coordinate[1] + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            blank = nr * N + nc
            if blank_array[blank] < 0:
                continue
            blank_array[blank] -= 1

    # print(temp_near_seat)
    # print(max_near)
    # print("seat_array : ", seat_array)
    # print("blank_array : ",blank_array)
    # print("student done\n")
    # break
total_satisfaction = 0
for idx, student in enumerate(seat_array):
    satisfied = 0
    r = idx // N
    c = idx % N
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            friend = nr * N + nc
            if seat_array[friend] in favorite_dict[student]:
                satisfied += 1
    if satisfied == 0:
        continue
    total_satisfaction += 10 ** (satisfied-1)

print(total_satisfaction)


