"""
Pierwsze rozwiązanie nie odporne na zakres liczb powyżej 10

print("".join(str(f"{i} Abracadabra\n") \
              for i in ("".join(str(i) for i in range(1, int(input()) + 1)))))
"""

for i in range(1, int(input())+1):
    print(f"{i} Abracadabra")
