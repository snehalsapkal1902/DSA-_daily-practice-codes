def count_odd(arr):
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
print("Odd count:", count_odd(arr))
