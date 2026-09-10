n,p1,p2,p3,t1,t2=map(int,input().split())
arr=[]
for _ in range (n):
    l,r=map(int,input().split())
    arr.append([l,r])
last=arr[n-1][1]
sm=0
for l,r in arr:
    sm+=(r-l)*p1
for i in range(n-1):
    ln=arr[i+1][0]-arr[i][1]
    get1=min(ln,t1)
    sm+=get1*p1
    ln-=get1
    get2=min(ln,t2)
    sm+=get2*p2
    ln-=get2
    sm+=ln*p3
print(sm)





