"""
Author :  Wooseok Jung
Problem_linK : https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""
def solution(k, dungeons):

    log = []
    visited = [0] * len(dungeons)
    def dfs(visited, num, count, array):

        if num == count:
            log.append(array)
            return

        for i in range(len(dungeons)):
            if not visited[i]:
                visited[i] = 1
                dfs(visited, num, count +1, array + [i])
                visited[i] = 0

    dfs(visited, len(dungeons), 0, [])

    max_count = -1
    print(log)
    for combi in log:
        current = k
        count = 0
        for dungeon_idx in combi:
            dun = dungeons[dungeon_idx]
            min_k = dun[0]
            cost_k = dun[1]

            if min_k <= current:
                current -= cost_k
                count += 1
            else:
                break
        max_count = max(max_count, count)

    print(max_count)

if __name__ == "__main__":
    solution(80, [[80,20],[50,40],[30,10]])