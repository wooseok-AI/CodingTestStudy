N = int(input())

data = []
for _ in range(N):
    name, score = input().split()
    data.append((name, int(score)))

def condition(data):
    return data[1]

def solution(data: list) -> list:

    # sorted_data = sorted(data, key=condition)
    sorted_data = sorted(data, key=lambda data: data[1])

    return sorted_data


print([x[0] for x in solution(data)])
