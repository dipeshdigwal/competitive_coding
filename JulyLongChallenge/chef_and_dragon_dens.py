def slope(n0, n1):
    return((int(H[n0-1])-int(H[n1-1]))/(n0-n1))


def maxGlide(start, stop):
    stringIndex = str(start)+","+str(stop)
    try:
        return(mem[stringIndex])
    except KeyError:
        if(start == stop):
            return(int(A[start-1]))
        elif(start < stop):
            maxGlideVal = 0
            sumGlide = int(A[start-1])
            maxSlope = -10e10
            for i in range(start+1, stop+1):
                s2 = slope(start, i)
                if(int(H[start-1]) > int(H[i-1])):
                    if(s2 >= maxSlope):
                        maxSlope = s2
                        x = maxGlide(i, stop)
                        if(x != -1):
                            sumGlide += x
                            if(sumGlide > maxGlideVal):
                                maxGlideVal = sumGlide
                            sumGlide -= x
                else:
                    sumGlide = -1
                    break

        else:
            maxGlideVal = 0
            sumGlide = int(A[start-1])
            minSlope = 10e10
            for i in range(start-1, stop-1, -1):
                s2 = slope(start, i)
                if(int(H[start-1]) > int(H[i-1])):
                    if(s2 <= minSlope):
                        minSlope = s2
                        x = maxGlide(i, stop)
                        if(x != -1):
                            sumGlide += x
                            if(sumGlide > maxGlideVal):
                                maxGlideVal = sumGlide
                            sumGlide -= x
                else:
                    sumGlide = -1
                    break

        if(sumGlide == -1):
            mem[stringIndex] = -1
            return(-1)
        mem[stringIndex] = maxGlideVal
        return(maxGlideVal)


def updater(b, c):
    global mem
    A[b-1] = str(c)
    #mem = {}
    mem2 = {}
    for i in mem.keys():
        x = i.split(",")
        start = int(x[0])
        stop = int(x[1])
        if(start < stop):
            if(b < start or b > stop):
                mem2[i] = mem[i]
        else:
            if(b > start or b < stop):
                mem2[i] = mem[i]
    mem = mem2


mem = {}
w = input().split(" ")
N = int(w[0])
Q = int(w[1])
H = input().split(" ")
A = input().split(" ")
for i in range(Q):
    X = input().split(" ")
    if(X[0] == "1"):
        updater(int(X[1]), int(X[2]))
    else:
        print(maxGlide(int(X[1]), int(X[2])))
