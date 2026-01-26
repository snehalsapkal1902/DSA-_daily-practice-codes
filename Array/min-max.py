#min-max

arr = [12, 5, 8, 130, 44, 2]

max_elem = arr[0]
min_elem = arr[0]

for num in arr:
    if num > max_elem:
        max_elem = num
    if num < min_elem:
        min_elem = num

print("Maximum element:", max_elem)
print("Minimum element:", min_elem)
