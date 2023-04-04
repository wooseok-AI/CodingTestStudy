from collections import deque, defaultdict

# 맵의 크기
N = int(input())
# 사과의 개수
K = int(input())
# 사과 위치 입력
apple = defaultdict(int)
for _ in range(K):
    apple_r, apple_c = map(int, input().split())
    apple[(apple_r - 1, apple_c - 1)] = True
# 명령의 개수
L = int(input())
order = defaultdict(int)
for _ in range(L):
    time, direction = input().split()
    order[int(time)] = direction

second = 0
snake = deque([(0, 0)])

dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# 재귀함수로 풀이하면 recursion오류가 난다...
def game(t: int, snake: deque, d: int):
    # 전진
    global second
    # print(snake)
    if order[t]:
        if order[t] == "L":
            # print("change to left")
            d = (d + 1) % 4
        elif order[t] == "D":
            # print("change to right")
            d = (d + 3) % 4

    second += 1
    nr, nc = (snake[0][0] + dxdy[d][0], snake[0][1] + dxdy[d][1])
    # print(nr," ", nc)
    if not 0 <= nr < N or not 0 <= nc < N or (nr, nc) in snake:
        # print("bump")
        return
    new_head = (nr, nc)
    if apple[new_head]:
        # print("eat apple")
        apple[new_head] = 0
    else:
        snake.pop()
    snake.appendleft((nr, nc))

    game(t + 1, snake, d)

while True:
    if order[second]:
        if order[second] == "L":
            # print("change to left")
            d = (d + 1) % 4
        elif order[second] == "D":
            # print("change to right")
            d = (d + 3) % 4

    second += 1
    nr, nc = (snake[0][0] + dxdy[d][0], snake[0][1] + dxdy[d][1])
    # print(nr," ", nc)
    if not 0 <= nr < N or not 0 <= nc < N or (nr, nc) in snake:
        # print("bump")
        break
    new_head = (nr, nc)
    if apple[new_head]:
        # print("eat apple")
        apple[new_head] = 0
    else:
        snake.pop()
    snake.appendleft((nr, nc))

game(0, snake, 3)
print(second)
