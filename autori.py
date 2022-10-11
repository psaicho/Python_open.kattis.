
#print(*filter(str.isupper,input()),sep="") #42 works and win


"""
1
print(*[c for c in input() if c.isupper()],sep="") // 50 works
2
print(*[c[0] for c in input().split("-")], sep="") // 50 works
3
print("".join(c[0] for c in input().split("-"))) // 48 works
4
print("".join(c for c in input() if c.isupper())) // 49 -Works
5
import re
print(*re.findall('[A-Z]',input()),sep="") // 52 works
6
print(''.join(filter(str.isupper,input()))) //43 work
7
print(*filter(str.isupper,input()),sep="") #42 works and win
8
print(*filter(lambda l: l.isupper(), input()),sep="") // 53 works
"""
