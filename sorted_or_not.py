recruited = []
P = 0


def factorial(N):
    prod = 1
    for i in range(2, N+1):
        prod *= i
    return(prod)


def recruitMinions(A, K, index):
    global P
    global recruited
    if(index == 0):
        P = 0
        recruited = []
    if(K == 0):
        P += 1
    else:
        for i in range(len(A)):
            if(index != 0):
                if(int(A[i]) >= recruited[index-1]):
                    recruited.append(int(A[i]))
                    recruitMinions(A[0:i]+A[i+1:len(A)], K-1, index+1)
                    recruited.pop()
            else:
                recruited.append(int(A[i]))
                recruitMinions(A[0:i]+A[i+1:len(A)], K-1, index+1)
                recruited.pop()


def gcd(a, b):
    if(a == 0):
        return(b)
    return(gcd(b % a, a))


def probablity(P2, Q2):
    x = gcd(P2, Q2)
    P = P2/x
    Q = Q2/x
    Q_inv = 1/(Q % (10e9+7))
    return((P*Q_inv) % (10e9+7))


a = input().split(" ")
N = int(a[0])
K = int(a[1])
A = input().split(" ")
Q = factorial(N)/factorial(N-K)
recruitMinions(A, K, 0)
print(probablity(P, Q))
