def power(N):
    Sum = 0
    for i in N:
        Sum += int(i)
    return(Sum)


def winner(A):
    a = A[0]
    b = A[1]
    pow_a = power(a)
    pow_b = power(b)
    if(pow_a > pow_b):
        Score[0] += 1
    elif(pow_a < pow_b):
        Score[1] += 1
    else:
        Score[0] += 1
        Score[1] += 1


T = int(input())
for i in range(T):
    N = int(input())
    Score = [0, 0]
    for j in range(N):
        A = input().split(" ")
        winner(A)
    if(Score[0] > Score[1]):
        print(str(0)+" "+str(Score[0]))
    elif(Score[0] < Score[1]):
        print(str(1)+" "+str(Score[1]))
    else:
        print(str(2)+" "+str(Score[0]))
