import numpy
R, C = map(int, input().split())
array = []
for i in range(0, R):
    print(i)
    f = input()
    array.append(list(map(int, [*f])))
    print(array)
N = int(input())
for j in range(N):
    r1, c1, r2, c2 = map(int, input().split())
    start = (array[r1 - 1][c2 - 1])
    while r1 - 1 < C:
        r1 - 1

# result if array[r1-1][c2-1] == array[r2-1][c2-1] == 0:
