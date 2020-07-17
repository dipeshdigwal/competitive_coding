def oddNumber(A):
    prod = 1
    for i in A:
        prod *= int(i)
    if(prod % 2 == 0):
        return("No")
    else:
        return("Yes")


T = int(input())
for i in range(T):
    N = int(input())
    A = input().split(" ")
    print(oddNumber(A))
