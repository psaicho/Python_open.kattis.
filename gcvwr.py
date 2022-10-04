G, T, N = map(int, input().split())
print(int(((G - T) * 0.9) - sum(list(map(int, input().split())))))
