import sys


p=input()
chrs=['H','Q','9']
for x in p:
    if x in chrs:
        print("YES")
        sys.exit()
print("NO")