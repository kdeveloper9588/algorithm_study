n = int(input())
arr = []
for i in range(n):
    i = int(input())
    arr.append(i)
arr.sort()
arr.reverse()
result = ' '.join(map(str, arr))  # 리스트 풀기[]랑','제거함
print(result)
