"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/169198
"""


def distance(x1, y1, x2, y2):
    return (x1-x2) ** 2 + (y1-y2) ** 2


def shortest(m, n, start_x, start_y, target_x, target_y):
    big_num = float('inf')
    up, down, left, right = big_num, big_num, big_num, big_num

    if not (start_x == target_x and start_y < target_y):
        up = distance(start_x, 2 * n - start_y, target_x, target_y)

    if not (start_x == target_x and start_y > target_y):
        down = distance(start_x, -start_y, target_x, target_y)

    if not (start_x > target_x and start_y == target_y):
        left = distance(-start_x, start_y, target_x, target_y)

    if not (start_x < target_x and start_y == target_y):
        right = distance(2 * m - start_x, start_y, target_x, target_y)

    return min(up, down, left, right)


def solution(m, n, start_x, start_y, balls):
    answer = []
    for target_x, target_y in balls:
        answer.append(shortest(m, n , start_x, start_y, target_x, target_y))

    return answer


m, n, start_x, start_y, balls = 10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]

print(solution(m, n, start_x, start_y, balls))
