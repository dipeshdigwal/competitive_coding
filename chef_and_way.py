from sys import setrecursionlimit

setrecursionlimit(10e5)


def bruteForce(A, K, flag):
    global maxi
    global prod
    if(len(A) == 0):
        if(prod < maxi):
            maxi = prod
    else:
        if(len(A) > K):
            looper = K
        else:
            looper = len(A)
        for i in range(looper):
            prod *= int(A[i])
            bruteForce(A[i+1:], K, 1)
            prod /= int(A[i])


def bruteForce_dp(A, i, K):
    try:
        return(memory[i])
    except KeyError:
        if((i+1) > len(A)):
            return(1)
        else:
            mini = 10e500000
            prod = 1
            if(i == 0):
                looper = 1
            else:
                if(i+K >= len(A)):
                    looper = len(A)
                else:
                    looper = i+K
            for j in range(i, looper):
                prod *= int(A[j])
                prod *= bruteForce_dp(A, j+1, K)
                if(prod < mini):
                    mini = prod
                prod = 1
            memory[i] = mini
            return(mini)


memory = {}
a = input().split(" ")
N = int(a[0])
K = int(a[1])
A = input().split(" ")
#maxi = 10e10
#prod = int(A[0])
#bruteForce(A[1:], K, 0)
#print(int(maxi) % (10e9+7))
print(bruteForce_dp(A, 0, K) % int(10e8+7))
