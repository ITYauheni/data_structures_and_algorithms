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


