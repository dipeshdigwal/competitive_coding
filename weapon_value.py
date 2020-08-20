def xor_gate_string(A,B): #represent a bitwise xor gate on two binary strings of same length 
    ans=""
    for i in range(len(A)):
        if(A[i]!=B[i]):
            ans+="1"
        else:
            ans+="0"
    return(ans)

def count_ones_string(A): #count the number of ones in a binary string
    sum=0
    for i in A:
        sum+=int(i)
    return(sum)

T=int(input())
for i in range(T):
    N=int(input())
    ans=""
    for j in range(N):
        S=input()
        if(j==0):
            ans=S
        else:
            ans=xor_gate_string(ans,S)
    print(count_ones_string(ans))