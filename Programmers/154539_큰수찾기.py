"""
Author : Wooseok Jung
Problem_link : https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""

def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    for idx in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[idx]:
            result[stack.pop()] = numbers[idx]
        stack.append(idx)
    return result

if __name__ == "__main__":
    numbers = list(map(int, input().split()))