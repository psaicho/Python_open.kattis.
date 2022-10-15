R, C = 4, 4
array = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]]
N = 1
Result = []
for j in range(N):
    r1, c1 = 0, 1
    person = int(array[r1][c1])
    Result = [[r1, c1]]
    for c in Result:
        x, y = c[0], c[1]
        if x < (R - 1) and array[x + 1][y] == person and [x + 1, y] not in Result:
            Result.append([x + 1, y])
        if y < (C - 1) and array[x][y + 1] == person and [x, y + 1] not in Result:
            Result.append([x, y + 1])
        if x > 0 and array[x - 1][y] == person and [x - 1, y] not in Result:
            Result.append([x - 1, y])
        if y > 0 and array[x][y - 1] == person and [x, y - 1] not in Result:
            Result.append([x, y - 1])


print(sorted(Result))
