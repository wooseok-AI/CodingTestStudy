"""
Author : Wooseok Jung
Problem_link = https://school.programmers.co.kr/learn/courses/30/lessons/131704
"""

from collections import deque
order = list(map(int, input().split()))

def solution(order):

    order = deque(order)
    stack = list()
    count = 0

    for package in range(1, len(order) + 1):
        stack.append(package)
        while stack:
            if stack[-1] == order[0]:
                order.popleft()
                stack.pop()
                count += 1
            else:
                break

    return count