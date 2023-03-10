def solution():
    N, K = map(int, input("M K :").split())
    count = 0

    while(N>1):
        if N%K == 0:
            N = N//K
            count += 1
        else:
            N -=1
            count += 1
    return count

if __name__ == "__main__":
    print(solution())