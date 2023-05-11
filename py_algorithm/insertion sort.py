arr = [7, 8, 9, 0, 3, 1, 2, 4, 5, 6]
arr2 = [7, 8, 9, 0, 3, 1, 2, 4, 5, 6]

for i in range(len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)
arr2.sort()
arr2.reverse()
print(arr2)
