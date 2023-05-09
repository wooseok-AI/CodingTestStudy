"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/118667
"""
from collections import deque

def compare(tot_q1, tot_q2):
    if tot_q1 > tot_q2:
        return "q1", "q2"
    return "q2", "q1"

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot_q1 = sum(queue1)
    tot_q2 = sum(queue2)

    data = {"q1" : [q1, tot_q1], "q2" : [q2, tot_q2]}
    total = tot_q1 + tot_q2

    if total % 2 != 0:
        return -1

    target = total // 2
    count = 0

    while True:
        if count > (len(q1) + len(q2)) * 2:
            return -1
        if data["q1"][1] == data["q2"][1]:
            break

        count += 1
        bigger, smaller = compare(data["q1"][1], data["q1"][2])
        pass_number = data[bigger][0].popleft()
        data[bigger][1] -= pass_number
        data[smaller][0].append(pass_number)
        data[smaller][1] += pass_number

    return count

solution([3, 2, 7, 2],[4, 6, 5, 1])