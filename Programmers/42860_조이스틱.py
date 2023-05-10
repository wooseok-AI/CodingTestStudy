
# 원하는 알파벳으로 변경하는 퇴단 거리 찾는 함수
def alphabet_distance(alpha):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # A인 경우 변경안해도 되므로 0
    if alpha == "A":
        return 0
    else:
        left_count = 0
        for i in range(1, len(alphabet)):
            if alphabet[i] == alpha:
                left_count = i
                break
        # 반대쪽의 거리는 (전체 알파벳 개수) - (왼쪽 이동거리)
        right_count = len(alphabet) - left_count

        return min(left_count, right_count)

# 현재 인덱스에서 다음 인덱스로 이동하는 최단거리 구하는 함수
# path : 이동 순서가 담긴 리스트
# full_length : 문자열의 총 길이 (길이 계산을 위해서)
def dist(path, full_length):
    dist = 0
    # 각 순서 별로 왼쪽 오른 쪽 거리를 구해서 최소값을 구함.
    for i in range(len(path)-1):
        one_way = abs(path[i] - path[i + 1])
        two_way = full_length - one_way
        dist += min(one_way, two_way)

    return dist


def solution(name):
    count = 0

    Not_A = []
    # 변경해야하는 알파벳을 찾기. idx를 저장
    for idx, n in enumerate(name):
        count += alphabet_distance(n)
        if n != "A" and idx !=0:
            Not_A.append(idx)

    # 저장된 idx를 토대로 변경하는 순열 구하기
    log = []
    visited = [0] * len(Not_A)

    def dfs(visited, num, count, array):
        if count == num:
            log.append(array)
            return
        for i in range(len(Not_A)):
            if not visited[i]:
                visited[i] = 1
                dfs(visited, num, count + 1, array + [Not_A[i]])
                visited[i] = 0
    dfs(visited, len(Not_A), 0, [0])
    # 경우의 수를 바탕으로 최단거리 구하기
    min_dist = float("inf")
    for path in log:
        min_dist = min(dist(path, len(name)), min_dist)
    print(count, min_dist)
    return count + min_dist
