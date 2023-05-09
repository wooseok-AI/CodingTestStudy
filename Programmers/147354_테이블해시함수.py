"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/147354
"""


def solution(data, col, row_begin, row_end):
    # 정렬
    new_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    mod_0 = sum([x % (row_begin) for x in new_data[row_begin - 1]])

    for i in range(row_begin, row_end):
        mod = sum([y % (i + 1) for y in new_data[i]])
        mod_0 = mod_0 ^ mod

    return mod_0