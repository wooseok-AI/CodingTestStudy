# -*- coding: utf-8 -*-
# 실전 문제 2: 위에서 아래로
# 3가지 내림차순 정렬 모두 구현
def selection_sort(array):
    N = len(array)

    for i in range(0, N):
        maximum_index = i
        for j in range(i, N):
            if array[j] > array[maximum_index]:
                array[j], array[maximum_index] = array[maximum_index], array[j]
            else:
                continue


def insertion_sort(array):
    N = len(array)

    for i in range(1, N):
        for j in range(i, 0, -1):
            if array[j] > array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                continue


def quick_sort(array: list, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:

        # 왼쪽에서 오른쪽으로 진행하며 pivot보다 작은 수 찾음
        while left <= end and array[left] > array[pivot]:
            left += 1
        # 오른쪽에서 왼으로 진행하며 pivot보다 큰 수 찾음
        while right > start and array[right] <= array[pivot]:
            right -=1

        # 교차했을경우 큰것을 pivot과 변경
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 교차 하지 않았을 경우 left right swap
        else:
            array[right], array[left] = array[left], array[right]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


if __name__ == "__main__":
    # N = int(input())
    # array = []
    # for _ in range(N):
    #     array.append(int(input()))
    original_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("Original array : ", original_array)

    selection_sort_array = original_array.copy()
    selection_sort(selection_sort_array)
    print("selection_sort : ", selection_sort_array)

    insertion_sort_array = original_array.copy()
    insertion_sort(insertion_sort_array)
    print("insertion_sort : ", insertion_sort_array)

    quick_sort_array = original_array.copy()
    quick_sort(quick_sort_array, 0, len(quick_sort_array) - 1)
    print("Quick_sort     : ", quick_sort_array)
