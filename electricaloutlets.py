for i in range(int(input())):
    l = list(map(int, input().split()))
    print(sum(l[1:]) - len(l) +2)

    """
    podejście mniej znakowe 
    for i in range(int(input())):print(sum(int(i)-1 for i in input().split()[1:])+1)
    """