def solution():
    N, M, K = map(int, input("N M K : ").split())
    data = list(map(int, input("numbers : ").split()))
    
    data.sort(reverse=True)
    first = data[0]
    second = data[1]

    max_count = K

    answer = 0
    count = 0
    addition = first

    if first == second:
        answer = first * M
    else:    
        while(M>0):
            if max_count == 0:
                addition = second
                print(addition, " ")
                answer += addition
                addition = first
                max_count = K
            else:
                print(addition, " ")
                answer += addition
                max_count -= 1
            M -= 1

    return answer

if __name__ == "__main__":
    print(solution())