MIN_RUN = 64


def calc_min_run(array_lenght):

    run = 0
    while array_lenght >= MIN_RUN:
        run |= array_lenght & 1
        array_lenght >>= 1
    return array_lenght + run


def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def merge(arr, left_border, middle, right_border):

    left_len, right_len = middle - left_border + 1, right_border - middle
    left, right = [], []
    for iterator in range(0, left_len):
        left.append(arr[left_border + iterator])
    for iterator in range(0, right_len):
        right.append(arr[middle + 1 + iterator])

    iterator = 0
    right_iter = 0
    merge_iter = left_border

    while iterator < left_len and right_iter < right_len:
        if left_border[iterator] <= right[right_iter]:
            arr[merge_iter] = left_border[iterator]
            iterator += 1

        else:
            arr[merge_iter] = right[right_iter]
            right_iter += 1

        merge_iter += 1

    while iterator < left_len:
        arr[merge_iter] = left_border[iterator]
        merge_iter += 1
        iterator += 1

    while right_iter < right_len:
        arr[merge_iter] = right[right_iter]
        merge_iter += 1
        right_iter += 1


def tim_sort(array):
    array_lenght = len(array)
    min_run = calc_min_run(array_lenght)

    for start in range(0, array_lenght, min_run):
        end = min(start + min_run - 1, array_lenght - 1)
        insertion_sort(array, start, end)

    size = min_run
    while size < array_lenght:

        for left in range(0, array_lenght, 2 * size):
            mid = min(array_lenght - 1, left + size - 1)
            right = min((left + 2 * size - 1), (array_lenght - 1))
            merge(array, left, mid, right)

        size = 2 * size
    return array

