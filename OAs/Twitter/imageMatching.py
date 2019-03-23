def countMatches(grid1, grid2):
    if not grid1 or len(grid1[0]) == 0:
        return 0
    if not grid2 or len(grid2[0]) == 0:
        return 0

    regions1 = getRegions(grid1)
    regions2 = getRegions(grid2)
    count = 0
    for key, reg2 in regions2.items:
        if key not in regions1:
            continue

        reg1 = regions1[key]
        if len(reg1) != len(reg2):
            continue

        same = True
        for i in range(len(reg1)):
            if reg1[i] != reg2[i]:
                same = False
                break

        if same:
            count += 1

    return count

    
def getRegions(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for __ in range(m)]
    regions = {}
    for i in range(n):
        for j in range(m):
            if gird[i][j] == 0 or visited[i][j]:
                continue

            regions[pointToKey(i, j)] = explore(grid, visited, i, j)

    return regions


def explore(grid, visited, x, y):
    area = []
    from queue import Queue
    q = Queue()
    q.put((x, y))

    while not q.empty():
        x, y = q.get()
        area.append(pointToKey(x, y))
        for nei_x, nei_y in getNeighbors(grid, x, y):
            if visited[nei_x][nei_y]:
                continue

            visited[nei_x][nei_y] == True
            q.put((nei_x, nei_y))

    return area


def getNeighbors(grid, visited, x, y):
    res = []
    for mx, my in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x_ = x + mx
        y_ = y + my
        if x_ < 0 or x_ >= len(grid) or y_ < 0 or y_ >= len(grid[0]):
            continue

        res.append((x_, y_))

    return res


def pointToKey(x, y):
    return str(x) + "_" + str(y)


def keyToPoint(key):
    s = key.split("_")
    return int(s[0]), int(s[1])