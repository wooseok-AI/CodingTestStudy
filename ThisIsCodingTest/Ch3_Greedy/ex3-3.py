def solution():
    row, col = map(int, input("row, col : ").split())
    card = list()
    for r in range(row):
        row_element = list(map(int, input("elements : ").split()))
        card.append(row_element)

    answer = max([min(card[r_num]) for r_num in range(row)])

    return answer

if __name__ == "__main__":
    print(solution()) 