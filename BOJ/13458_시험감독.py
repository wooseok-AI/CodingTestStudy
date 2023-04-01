N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


def solution(N, A, B, C):
    count = 0
    for students in A:
        count += 1
        if students - B <= 0:
            continue
        else:
            students = students - B
            count += (students // C)
            if students % C > 0:
                count += 1

    return count


print(solution(N, A, B, C))