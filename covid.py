def find_chain(X):
    mini = len(X)
    maxi = 1
    chain = 1
    for i in range(1, len(X)):
        c = int(X[i])-int(X[i-1])
        if(c <= 2):
            chain += 1
        else:
            if(chain < mini):
                mini = chain
            if(chain > maxi):
                maxi = chain
            chain = 1
    if(chain < mini):
        mini = chain
    if(chain > maxi):
        maxi = chain
    return(str(mini)+" "+str(maxi))


t = int(input())
for i in range(int(t)):
    n = input()
    X = input().split(" ")
    print(find_chain(X))
