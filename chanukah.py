def c(k):
    a, b, = 2, 1
    suma = a
    for i in range(1, k):
        a = a + b
        suma += a
    return suma



for i in range(1, int(input()) + 1):
    X, Y = map(int, input().split())
    print(f"{X} {c(Y)}")
