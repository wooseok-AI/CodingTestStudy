"""
Author : Wooseok Jung
Problem_link : https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""

answer = 0
log = []
data = [1, -1]


def dfs(numbers, target, count, result):
    global answer
    if count == len(numbers):
        temp = 0
        for idx, x in enumerate(numbers):
            temp += x * result[idx]
        if temp == target:
            answer += 1
        return

    for i in range(len(data)):
        dfs(numbers, target, count + 1, result + [data[i]])


def solution(numbers, target):
    dfs(numbers, target, 0, [])
    return answer