class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class Stack:
    def __init__(self):
        self.stack = []
        self.N = 0

    def stackInserter(self, X, Y):
        if(self.N == 0):
            self.stack.append([Point(X, Y)])
            self.N += 1
        else:
            for i in range(len(self.stack)):
                for j in range(len(self.stack[i])):
                    if(self.stack[i][j].X == X or self.stack[i][j].Y == Y):
                        self.stack[i].append(Point(X, Y))
                        self.N += 1
                        if(len(self.stack[i]) == 4):
                            self.stack.pop(i)
                        return(1)
            self.stack.append([Point(X, Y)])
            self.N += 1
        return(1)

    def pointRetriever(self):
        X = []
        Y = []
        for i in range(len(self.stack[0])):
            if(self.stack[0][i].X not in X):
                X.append(self.stack[0][i].X)
            else:
                X.remove(self.stack[0][i].X)
            if(self.stack[0][i].Y not in Y):
                Y.append(self.stack[0][i].Y)
            else:
                Y.remove(self.stack[0][i].Y)
        print(str(X[0])+" "+str(Y[0]))


T = int(input())
for i in range(T):
    N = int(input())
    S = Stack()
    for j in range((4*N)-1):
        P = input().split(" ")
        S.stackInserter(int(P[0]), int(P[1]))
    S.pointRetriever()
