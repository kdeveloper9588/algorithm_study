d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
# bottom up dp
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]
