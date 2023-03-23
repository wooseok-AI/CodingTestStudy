def solution(N):
    time = [0, 0, 0]
    count = 0

    for hour in range(N +1):
        for min in range(60):
            for sec in range(60):
                if "3" in str(hour) + str(min) + str(sec):
                    count +=1

    return count


if __name__ == "__main__":
    N = int(input("Number : "))
    print(solution(N))
