"""
Author : Wooseok Jung
Problem_link : https://school.programmers.co.kr/learn/courses/30/lessons/60057
"""

def compress(s, bind):
    start = 0
    end = 0 + bind
    iter = len(s) // bind + 1
    result = ""

    prev = ""
    for i in range(iter):
        now = s[start:end]
        if not prev:
            prev = now
            count = 1
            start, end = start + bind, end + bind
            continue
        if prev:
            if now == prev:
                count += 1
            else:
                if count > 1:
                    result += str(count)
                result += prev
                prev = now
                count = 1
        start, end = start + bind, end + bind

    if count > 1:
        result += str(count)
    result += now

    return result


def solution(s):
    answer = 0
    min_length = 9999

    for bind in range(1, len(s) + 1):
        result = compress(s, bind)
        min_length = min(min_length, len(result))

    return min_length

if __name__ == "__main__":
    s = input()
    solution(s)