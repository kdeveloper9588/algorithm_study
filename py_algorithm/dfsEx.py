n, m = map(int, input().split())

world = []
for i in range(n):
    world.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if world[x][y] == 0:
        world[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


rs = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            rs += 1
print(rs)
