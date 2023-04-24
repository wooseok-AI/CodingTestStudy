"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""


def solution(people, limit):
    people.sort()

    count = 0
    minimum = 0
    maximum = len(people) - 1

    while minimum <= maximum:
        if people[maximum] + people[minimum] <= limit:
            minimum += 1
        count += 1
        maximum -= 1

    return count

if __name__ == "__main__":
    people = list(map(int, input().split()))
    limit = int(input())
    print(solution(people, limit))
