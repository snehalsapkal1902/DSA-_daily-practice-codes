def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0  # slow pointer

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i + 1  # new length


arr = [1,1,0,0,4,3,3]
n = remove_duplicates(arr)

print(arr[:n])  # [1, 2, 3, 4]
