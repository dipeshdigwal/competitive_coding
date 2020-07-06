def f_minimizer(n):
    a=[1,1,n-2]
    f=abs(a[0]-a[1])+abs(a[1]-a[2])+abs(a[0]-a[2])

n=int(input())
for i in range(n-1):
    k=input().split(" ")