n=int(input())
home=input()
left=0
right=0
for _ in range(n):
    s=input().split('->')
    if s[0]==home:
        left+=1
    if s[1]==home:
        right+=1
if left==right:
    print("home")
else:
    print("contest")