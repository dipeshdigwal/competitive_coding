from math import fabs


def guitarStrings(A):
    Sum = 0
    prev = int(A[0])
    for i in range(1, len(A)):
        Sum += fabs(int(A[i])-prev)-1
        prev = int(A[i])
    return(int(Sum))


T = int(input())
for i in range(T):
    N = int(input())
    S = input().split(" ")
    print(guitarStrings(S))
