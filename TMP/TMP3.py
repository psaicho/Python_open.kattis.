def c(k):
    a = 2
    suma = a
    for i in range(1, k):
        suma += a + 1
        a += 1
    return suma


print(c(8))
for i in range(1, int(input()) + 1):
    X, Y = map(int, input().split())
    print(f"{X} {c(Y)}")