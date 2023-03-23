"""
풀이
"""


def solution(position):
    row, col = int(position[-1]), int("abcdefgh".index(position[0])) + 1
    count = 0
    # UP
    if row - 2 >= 1:
        # LEFT
        if col - 1 >= 1:
            count += 1
        # Right
        if col + 1 <= 8:
            count += 1

    # DOWN
    if row + 2 <= 8:
        # LEFT
        if col - 1 >= 1:
            count += 1
        if col + 1 <= 8:
            count += 1
    # RIGHT
    if col - 2 >= 1:
        # LEFT
        if row - 1 >= 1:
            count += 1
        # Right
        if row + 1 <= 8:
            count += 1

            # DOWN
    if col + 2 <= 8:
        # LEFT
        if row - 1 >= 1:
            count += 1
        if row + 1 <= 8:
            count += 1
    return count


"""
모범답안
"""


def absolute_solution(position):
    row, col = int(position[-1]), int("abcdefgh".index(position[0])) + 1

    count = 0
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]
        if 1 <= next_row <= 8 and 1 <= next_col <= 8:
            count += 1
    return count


if __name__ == "__main__":
    position = input("position : ")
    print(solution(position))
    print(absolute_solution(position))
