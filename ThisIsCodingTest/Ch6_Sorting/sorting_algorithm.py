
# 선택 정렬
def selection_sort(array: list):
    N = len(array)
    for i in range(N):
        minimum_index = i
        for j in range(i+1, N):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[minimum_index], array[i] = array[i], array[minimum_index]


# 삽입 정렬
def insertion_sort(array: list):
    N = len(array)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                continue


# 퀵 정렬
def quick_sort(array: list, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽에서 출발하여 pivot보다 큰 수 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서 출발하여 pivot보다 작은 수 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
        # left가 right를 지나쳤을 경우, right와 pivot 교체
        else:
            array[pivot], array[right] = array[right], array[pivot]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)



# 계수 정렬
def count_sort(array: list):

    data = [0] * (max(array) + 1)

    for i in range(len(array)):
        data[array[i]] += 1

    result = [i for i in range(len(array)) if data[i] != 0]

    return result




if __name__ == "__main__":

    original_array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print("Original array : ", original_array)

    selection_sort_array = original_array.copy()
    selection_sort(selection_sort_array)
    print("selection_sort : ", selection_sort_array)

    insertion_sort_array = original_array.copy()
    insertion_sort(insertion_sort_array)
    print("insertion_sort : ", insertion_sort_array)

    quick_sort_array = original_array.copy()
    quick_sort(quick_sort_array, 0, len(quick_sort_array)-1)
    print("Quick_sort     : ", quick_sort_array)

    count_sort_array = original_array.copy()
    count_sort_array = count_sort(count_sort_array)
    print("Count_sort     : ", count_sort_array)
