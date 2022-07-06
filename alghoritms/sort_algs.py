def selection_sort(arr, *, reverse=False):
    alg = max if reverse else min

    try:
        iter(arr)
    except TypeError:
        raise TypeError(f"{type(arr)} is not iterable")

    length = len(arr)
    if length == 0:
        return arr

    for i in range(length - 1):
        tmp = arr[i]
        index_min = i

        for j in range(i+1, length):
            if tmp != alg(tmp, arr[j]):
                tmp = arr[j]
                index_min = j

        if i != index_min:
            arr[i], arr[index_min] = arr[index_min], arr[i]

    return arr


def insertion_sort(arr, *, reverse=False):
    len_ = len(arr)
    alg = min if reverse else max

    for i in range(1, len_):
        for j in range(i, 0, -1):
            if arr[j] != alg(arr[j], arr[j-1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return arr


def bubble_sort(arr, *, reverse=False):
    len_ = len(arr)
    alg = max if reverse else min

    for i in range(len_-1):
        for j in range(len_-1-i):
            if arr[j] != alg(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
