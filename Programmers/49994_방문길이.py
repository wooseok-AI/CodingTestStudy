"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/49994
"""


def coord_to_node(coord):
    return (coord[0] + 5) + (5 - coord[1]) * 11


def solution(dirs):
    d_dict = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0] * 121 for _ in range(121)]

    coord = (0, 0)
    count = 0
    for dir in dirs:
        x, y = coord[0], coord[1]
        d = d_dict[dir]
        nx = x + dx[d]
        ny = y + dy[d]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            current_n = coord_to_node(coord)
            next_n = coord_to_node((nx, ny))

            if not visited[current_n][next_n]:
                visited[current_n][next_n] = 1
                visited[next_n][current_n] = 1
                count += 1

            coord = (nx, ny)

    return count