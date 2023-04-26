"""
Author : Wooseok Jung
Problem_link : https://school.programmers.co.kr/learn/courses/30/lessons/77484
"""


def solution(lottos, win_nums):
    zeros = 0
    set_lottos = set(tuple(lottos))
    set_win_nums = set(tuple(win_nums))

    if len(set_lottos) != len(lottos):
        zeros = 6 - len(set_lottos) + 1

    correct = len(set_lottos & set_win_nums)

    if zeros == 0 and correct != 6:
        zeros = 1

    minimum = abs(correct - 7)
    maximum = abs((correct + zeros) - 7)

    if minimum >= 6: minimum = 6
    if maximum >= 6: maximum = 6

    return [maximum, minimum]


def another_solution(lottos, win_nums):
    correct = 0
    zeros = 0
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1 }
    for i in range(6):
        if lottos[i] == 0:
            zeros += 1
        elif lottos[i] in win_nums:
            correct += 1

    minimum = rank[correct]
    maximum = rank[correct + zeros]

    return  [maximum, minimum]



if __name__ == "__main__":
    lottos = list(map(int, input().split()))
    win_nums = list(map(int, input().split()))

    solution(lottos, win_nums44)