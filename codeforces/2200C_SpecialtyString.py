t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if n%2==1:
        print('NO')
        continue
    stack=[]
    for c in s:
        if stack and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack)==0:
        print("YES")
    else:
        print("NO")



