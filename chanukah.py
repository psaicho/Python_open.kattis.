def c(k):
    a, b, = 2, 1
    suma = a
    for i in range(1, k):
        a = a + b
        suma += a
    return suma


N = []
for i in range(1, int(input()) + 1):
    X, Y = map(int, input().split())
    N.append([X, c(Y)])
for j in N:
    print(f"{j[0]} {j[1]}")
