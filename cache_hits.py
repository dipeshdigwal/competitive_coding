def num_cache_hits(B,X):
    flag=None
    sum_cache_hits=0
    for j in X:
        block=int(int(j)/B)
        if(block!=flag):
            sum_cache_hits+=1
        flag=block
    return(sum_cache_hits)

T=int(input())
for i in range(T):
    a=input().split(" ")
    [N,B,M]=[int(i) for i in a]
    X=input().split(" ")
    print(num_cache_hits(B,X))