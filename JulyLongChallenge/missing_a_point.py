

class Dict:
    def __init__(self):
        self.d_X = {}
        self.d_Y = {}

    def insert(self, X, Y):
        try:
            self.d_X.pop(X)
        except KeyError:
            self.d_X[X] = 1

        try:
            self.d_Y.pop(Y)
        except KeyError:
            self.d_Y[Y] = 1

    def get(self):
        for i in self.d_X.keys():
            x = i
        for i in self.d_Y.keys():
            y = i
        print(str(x)+" "+str(y))


T = int(input())
for i in range(T):
    N = int(input())
    S = Dict()
    for j in range((4*N)-1):
        P = input().split(" ")
        S.insert(int(P[0]), int(P[1]))
    S.get()
