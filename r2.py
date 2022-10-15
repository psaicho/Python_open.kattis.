i,y = map(int, input().split())
print(y-(i-y) if i>y else y+(y-i))