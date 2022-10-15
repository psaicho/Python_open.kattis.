R, C = map(int, input().split())
a = []
for i in range(R):
    f = input()
    a.append(list(map(int, [*f])))
N = int(input())
for j in range(N):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    P = int(a[r1][c1])
    D = [[r1, c1]]
    if r1 == r2 and c1 == c2:
        print("decimal" if P == 1 else "binary")
        break
    else:
        for c in D:
            if [r2, c2] in D: break
            x, y = c[0], c[1]
            if x < (R - 1) and a[x + 1][y] == P and [x + 1, y] not in D: D.append([x + 1, y])
            if y < (C - 1) and a[x][y + 1] == P and [x, y + 1] not in D: D.append([x, y + 1])
            if x > 0 and a[x - 1][y] == P and [x - 1, y] not in D: D.append([x - 1, y])
            if y > 0 and a[x][y - 1] == P and [x, y - 1] not in D: D.append([x, y - 1])

    if (r1 == r2 and c1 == c2 and P == 1) or ([r2, c2] in D and P == 1):
        print("decimal")
    elif (r1 == r2 and c1 == c2 and P == 1) or ([r2, c2] in D and P == 0):
        print("binary")
    else:
        print("neither")
