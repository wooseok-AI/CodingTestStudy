"""

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100월 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원 일때, 거슬러줘야할 동전의 최소 개수를 구하라. 단, 거슬러 줘야할 돈 N은 항상 10의 배수이다.

"""

def solution(N):
    coin_count = 0
    coin = [500, 100, 50, 10]
    change = N
    for c in coin:
        coin_count+=change//c
        change = change%c

    return coin_count

if __name__ == "__main__":
    N = int(input("거슬러줘야 할 돈 : "))
    print(solution(N))
