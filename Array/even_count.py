def count_even(arr):
    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
    return count

arr = [12, 7, 5, 8, 10, 3, 6]
print("Count of even elements =", count_even(arr))
