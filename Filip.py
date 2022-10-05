x, y = input().split()
print(x[::-1] if int(x[::-1]) > int(y[::-1]) else y[::-1])
