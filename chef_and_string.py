def formPairs(S):
    sum = 0
    C = ""
    for i in S:
        if(C == ""):
            C = i
        elif(C == "x" and i == "y"):
            C = ""
            sum += 1
        elif(C == "y" and i == "x"):
            C = ""
            sum += 1
    return(sum)


T = int(input())
for i in range(T):
    S = input()
    print(formPairs(S))
