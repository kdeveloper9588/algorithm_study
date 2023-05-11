arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(arr)+1)
print(len(arr))
for i in range(len(arr)):
    count[arr[i]] += 1  # i= 7이면 count의 7번째 배열 개수 1올림

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
