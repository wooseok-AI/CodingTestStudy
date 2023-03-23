def solution(size, order_list):
    row, col = 1, 1

    for order in order_list:
        if order == "R" and col < size:
            col += 1
        elif order == "L" and col > 1:
            col -= 1
        elif order == "U" and row > 1:
            row -= 1
        elif order == "D" and row < size:
            row += 1

    print(row, " ", col)
    return None


if __name__ == "__main__":
    size = int(input("map size : "))
    order_list = list(input("order : ").split())
    solution(size, order_list)
