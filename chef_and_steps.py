def traversableSteps(A, K):
    stri = ""
    for i in A:
        if(int(i) % K == 0):
            stri += "1"
        else:
            stri += "0"
    print(stri)


T = int(input())
for i in range(T):
    a = input().split(" ")
    N = int(a[0])
    K = int(a[1])
    D = input().split(" ")
    traversableSteps(D, K)
